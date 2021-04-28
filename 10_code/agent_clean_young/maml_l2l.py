#!/usr/bin/env python3

"""
Trains a 2-layer MLP with MAML-VPG augmented with the DiCE objective.

Usage:

python examples/rl/maml_dice.py
"""

import random
from pathlib import Path
import cherry as ch
import gym
import numpy as np
import torch
from cherry.algorithms import a2c
from cherry.models.robotics import LinearValue
from torch import optim
from tqdm import tqdm
from gym import spaces

import learn2learn as l2l
import policy
# from policies import DiagNormalPolicy

import citylearn


def weighted_cumsum(values, weights):
    for i in range(values.size(0)):
        values[i] += values[i - 1] * weights[i]
    return values


def compute_advantages(baseline, tau, gamma, rewards, dones, states, next_states):
    # Update baseline
    returns = ch.td.discount(gamma, rewards, dones)
    baseline.fit(states, returns)
    values = baseline(states)
    next_values = baseline(next_states)
    bootstraps = values * (1.0 - dones) + next_values * dones
    next_value = torch.zeros(1, device=values.device)
    return ch.pg.generalized_advantage(tau=tau,
                                       gamma=gamma,
                                       rewards=rewards,
                                       dones=dones,
                                       values=bootstraps,
                                       next_value=next_value)


def maml_a2c_loss(train_episodes, learner, baseline, gamma, tau):
    # Update policy and baseline
    states = train_episodes.state()
    actions = train_episodes.action()
    rewards = train_episodes.reward()
    dones = train_episodes.done()
    next_states = train_episodes.next_state()
    log_probs = learner.log_prob(states, actions)
    weights = torch.ones_like(dones)
    weights[1:].add_(-1.0, dones[:-1])
    weights /= dones.sum()
    cum_log_probs = weighted_cumsum(log_probs, weights)
    advantages = compute_advantages(baseline, tau, gamma, rewards,
                                    dones, states, next_states)
    return a2c.policy_loss(l2l.magic_box(cum_log_probs), advantages)


def main(
        experiment='dev',
        adapt_lr=0.1,
        meta_lr=0.001,
        adapt_steps=1,
        num_iterations=20,
        meta_bsz=20,
        adapt_bsz=20,
        tau=1.00,
        gamma=0.99,
        num_workers=8,
        seed=42,
):
    # parameter for citylearn
    climate_zone = 4
    data_path = Path("data/Climate_Zone_"+str(climate_zone))
    building_attributes = data_path / 'building_attributes.json'
    weather_file = data_path / 'weather_data.csv'
    solar_profile = data_path / 'solar_generation_1kW.csv'
    building_state_actions = 'buildings_state_action_space.json'
    building_id = ["Building_1"]
    objective_function = ['ramping','1-load_factor','average_daily_peak',\
                        'peak_demand','net_electricity_consumption','quadratic']
    # register an city_learn envirnoment
    # TODO might need to change max_episode_Steps
    gym.envs.register(
        id='citylearn-v0',
        entry_point='gym.envs.classic_control:citylearn.CityLearn',
        max_episode_steps=150,
        kwargs={'data_path' : data_path, 'building_attributes' : building_attributes, \
            'weather_file' : weather_file, 'solar_profile': solar_profile, \
                "building_state_actions":building_state_actions, "simulation_period":(0,8759),\
                    "objective_function":objective_function},
    )
    def make_env():
        '''
        set environment
        '''
        # Load environment
        climate_zone = 4
        data_path = Path("data/Climate_Zone_"+str(climate_zone))
        building_attributes = data_path / 'building_attributes.json'
        weather_file = data_path / 'weather_data.csv'
        solar_profile = data_path / 'solar_generation_1kW.csv'
        building_state_actions = 'buildings_state_action_space.json'
        building_id = ["Building_1"]
        objective_function = ['ramping','1-load_factor','average_daily_peak',\
                            'peak_demand','net_electricity_consumption','quadratic']

        # Contain the lower and upper bounds of the states and actions, to be provided to the agent to normalize the variables between 0 and 1.
        # Can be obtained using observations_spaces[i].low or .high
        env = gym.make("citylearn-v0")

        observations_space, actions_space = env.get_state_action_spaces()
        # observations_spaces, actions_spaces = env.get_state_action_spaces()
        # TODO: need to change when we do multiple buildings
        action_spaces = {"0": a_space for uid, a_space in zip(building_id, actions_space)}
        action_dim = action_spaces["0"].shape[0]
        observation_spaces = {"0":o_space for uid, o_space in zip(building_id, observations_space)}
        state_dim = observation_spaces["0"].shape[0]
        # Provides information on Building type, Climate Zone, Annual DHW demand, Annual Cooling Demand, Annual Electricity Demand, Solar Capacity, and correllations among buildings
        # building_info = env.get_building_information()
        # print (env.buildings)
        # print (observations_spaces, actions_spaces = env.get_state_action_spaces())
        building_num = env.buildings
        return (env, action_spaces, action_dim, state_dim)

    env, action_spaces, action_dim, state_dim = make_env()
    env = l2l.gym.AsyncVectorEnv([env for _ in range(num_workers)])
    env.seed(seed)
    env = ch.envs.Torch(env)
    
    #TODO: PolicyNetwork(state_dim, action_dim, self.action_spaces[uid], \
    # self.action_scaling_coef, hidden_dim).to(self.device)
    #TODO: I need to incorporate a code where it we amek policy by its states and actionspace
    # for each building.
    policy = policy.PolicyNetwork(state_dim, action_dim, action_spaces)
    meta_learner = l2l.algorithms.MAML(policy, lr=adapt_lr)
    baseline = LinearValue(env.state_size, env.action_size)
    opt = optim.Adam(policy.parameters(), lr=meta_lr)
    all_rewards = []

    for iteration in range(num_iterations):
        iteration_loss = 0.0
        iteration_reward = 0.0
        for task_config in tqdm(env.sample_tasks(meta_bsz), leave=False, desc='Data'):  # Samples a new config
            learner = meta_learner.clone()
            env.set_task(task_config)
            env.reset()
            task = ch.envs.Runner(env)

            # Fast Adapt
            for step in range(adapt_steps):
                train_episodes = task.run(learner, episodes=adapt_bsz)
                loss = maml_a2c_loss(train_episodes, learner, baseline, gamma, tau)
                learner.adapt(loss)

            # Compute Validation Loss
            valid_episodes = task.run(learner, episodes=adapt_bsz)
            loss = maml_a2c_loss(valid_episodes, learner, baseline, gamma, tau)
            iteration_loss += loss
            iteration_reward += valid_episodes.reward().sum().item() / adapt_bsz

        # Print statistics
        print('\nIteration', iteration)
        adaptation_reward = iteration_reward / meta_bsz
        print('adaptation_reward', adaptation_reward)
        all_rewards.append(adaptation_reward)

        adaptation_loss = iteration_loss / meta_bsz
        print('adaptation_loss', adaptation_loss.item())

        opt.zero_grad()
        adaptation_loss.backward()
        opt.step()


if __name__ == '__main__':
    main()
