import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Independent, Normal

from collections import OrderedDict

def weight_init(module):
    if isinstance(module, nn.Linear):
        nn.init.xavier_uniform_(module.weight)
        module.bias.data.zero_()

class Policy(nn.Module):
    def __init__(self, input_size, output_size):
        super(Policy, self).__init__()
        self.input_size = input_size
        self.output_size = output_size

        # For compatibility with Torchmeta
        self.named_meta_parameters = self.named_parameters
        self.meta_parameters = self.parameters

    def update_params(self, loss, params=None, step_size=0.5, first_order=False):
        """
        Apply one step of gradient descent on the loss function `loss`, with 
        step-size `step_size`, and returns the updated parameters of the neural 
        network.
        """
        if params is None:
            params = OrderedDict(self.named_meta_parameters())

        grads = torch.autograd.grad(loss, params.values(),
                                    create_graph=not first_order)

        updated_params = OrderedDict()
        for (name, param), grad in zip(params.items(), grads):
            updated_params[name] = param - step_size * grad

        return updated_params

class NormalMLPPolicy(Policy):
    """
    Policy network based on a multi-layer perceptron (MLP), with a 
    `Normal` distribution output, with trainable standard deviation. This 
    policy network can be used on tasks with continuous action spaces
    """

    def __init__(self,input_size,output_size,hidden_sizes=(100, 100),nonlinearity=F.relu,\
        init_std=1.0,min_std=1e-6):
        super(NormalMLPPolicy, self).__init__(input_size=input_size,
                                              output_size=output_size)
        self.hidden_sizes = hidden_sizes
        self.nonlinearity = nonlinearity
        self.min_log_std = math.log(min_std)
        self.num_layers = len(hidden_sizes) + 1

        layer_sizes = (input_size,) + hidden_sizes
        # adding different layers
        for i in range(1, self.num_layers):
            self.add_module('layer{0}'.format(i),nn.Linear(layer_sizes[i - 1], layer_sizes[i]))
        # Calculating mean and std of normal distribution
        self.mu = nn.Linear(layer_sizes[-1], output_size)
        self.sigma = nn.Parameter(torch.Tensor(output_size))
        self.sigma.data.fill_(math.log(init_std))
        '''
        Pass an initialization function to torch.nn.Module.apply. 
        It will initialize the weights in the entire nn.Module recursively.
        '''
        self.apply(weight_init)

    def forward(self, input, params=None):
        if params is None:
            params = OrderedDict(self.named_parameters())

        output = input
        for i in range(1, self.num_layers):
            output = F.linear(output,weight=params['layer{0}.weight'.format(i)],\
                bias=params['layer{0}.bias'.format(i)])
            output = self.nonlinearity(output)

        mu = F.linear(output,
                      weight=params['mu.weight'],
                      bias=params['mu.bias'])
        scale = torch.exp(torch.clamp(params['sigma'], min=self.min_log_std))
        # https://bochang.me/blog/posts/pytorch-distributions/ to know more about Independent class
        # sort of reshaping the distribution
        return Independent(Normal(loc=mu, scale=scale), 1)

class PolicyNetwork(nn.Module):
    def __init__(self, num_inputs, num_actions, action_space, action_scaling_coef=1, hidden_dim=[400,300],
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

