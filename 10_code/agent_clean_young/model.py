import os
import torch.optim as optim
import torch
import torch.nn.functional as F
import torch.nn as nn
from torch.distributions import Normal
from torch.optim import Adam
import numpy as np
import random
import copy
import gym
from sklearn.linear_model import LinearRegression
import json
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingRegressor
# torch.autograd.set_detect_anomaly(True)
import time
import math

class PolicyNetwork(nn.Module):
    def __init__(self, num_inputs, num_actions, action_space, action_scaling_coef, hidden_dim=[400,300],
                 init_w=3e-3, log_std_min=-20, log_std_max=2, epsilon = 1e-6):
        super(PolicyNetwork, self).__init__()

        self.log_std_min = log_std_min
        self.log_std_max = log_std_max
        self.epsilon = epsilon
        
        self.linear1 = nn.Linear(num_inputs, hidden_dim[0])
        self.linear2 = nn.Linear(hidden_dim[0], hidden_dim[1])

        self.mean_linear = nn.Linear(hidden_dim[1], num_actions)
        self.log_std_linear = nn.Linear(hidden_dim[1], num_actions)

        self.mean_linear.weight.data.uniform_(-init_w, init_w)
        self.mean_linear.bias.data.uniform_(-init_w, init_w)

        self.log_std_linear.weight.data.uniform_(-init_w, init_w)
        self.log_std_linear.bias.data.uniform_(-init_w, init_w)

        self.action_scale = torch.FloatTensor(
            action_scaling_coef * (action_space.high - action_space.low) / 2.)
        self.action_bias = torch.FloatTensor(
            action_scaling_coef * (action_space.high + action_space.low) / 2.)

    def forward(self, state):
        x = F.relu(self.linear1(state))
        x = F.relu(self.linear2(x))
        mean = self.mean_linear(x)
        log_std = self.log_std_linear(x)
        log_std = torch.clamp(log_std, min=self.log_std_min, max=self.log_std_max)
        return mean, log_std

    def sample(self, state):
        mean, log_std = self.forward(state)
        std = log_std.exp()
        normal = Normal(mean, std)
        x_t = normal.rsample()  # for reparameterization trick (mean + std * N(0,1))
        y_t = torch.tanh(x_t)
        action = y_t * self.action_scale + self.action_bias
        log_prob = normal.log_prob(x_t)
        # Enforcing Action Bound
        log_prob -= torch.log(self.action_scale * (1 - y_t.pow(2)) + self.epsilon)
        log_prob = log_prob.sum(1, keepdim=True)
        mean = torch.tanh(mean) * self.action_scale + self.action_bias
        return action, log_prob, mean

    def to(self, device):
        self.action_scale = self.action_scale.to(device)
        self.action_bias = self.action_bias.to(device)
        return super(PolicyNetwork, self).to(device)


class SoftQNetwork(nn.Module):
    def __init__(self, num_inputs, num_actions, hidden_size=[400,300], init_w=3e-3):
        super(SoftQNetwork, self).__init__()
        
        self.linear1 = nn.Linear(num_inputs + num_actions, hidden_size[0])
        self.linear2 = nn.Linear(hidden_size[0], hidden_size[1])
        self.linear3 = nn.Linear(hidden_size[1], 1)
        self.ln1 = nn.LayerNorm(hidden_size[0])
        self.ln2 = nn.LayerNorm(hidden_size[1])
        
        self.linear3.weight.data.uniform_(-init_w, init_w)
        self.linear3.bias.data.uniform_(-init_w, init_w)
        
    def forward(self, state, action):
        x = torch.cat([state, action], 1)
        x = self.ln1(F.relu(self.linear1(x)))
        x = self.ln2(F.relu(self.linear2(x)))
        x = self.linear3(x)
        return x

class RegressionBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.x = []
        self.y = []
        self.position = 0
    
    def push(self, variables, targets):
        if len(self.x) < self.capacity and len(self.x)==len(self.y):
            self.x.append(None)
            self.y.append(None)
        
        self.x[self.position] = variables
        self.y[self.position] = targets
        self.position = (self.position + 1) % self.capacity
    
    def __len__(self):
        return len(self.x)