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

class ReplayBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.position = 0
    
    def push(self, state, action, reward, next_state, done):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        
        self.buffer[self.position] = (state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity
    
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = map(np.stack, zip(*batch))
        return state, action, reward, next_state, done
    
    def __len__(self):
        return len(self.buffer)