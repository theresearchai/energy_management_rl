Shota Takeshima: In this document, I write the report of what I have done this week, and mention the goal next week. **Based on the feedback of last week's report and goal, I add comments on how you and your group work together to work on this tasks..**

## Report: week 6&7 2/22 ~ 3/5

In our storyboad, the current theme is still corresponding to **Theme 1.3**.

> We will start implementing algorithms into city-learn or different simulators and evaluate the performance for each algorithms. 

Thinking about the evaluation, the comparison baselines are needed. The first one is the SAC multiple-agents included in CityLean. The benefit of MAML is that we can get a good policy for an unknown task after training for a short duration. We confirm how the original SAC multiple-agents work against the unknown task (different types of buildings) for a short training. (Hopefully, we want to get a bad result.) Another baseline is REINFORCE multiple-agents. There are two main types of reinforcement learning algorithms, such as on-policy and off-policy approaches. SAC is a subclass of the off-policy, and MAM is a subclass of on-policy. So, although it depends on the problem, there is a possibility that the result obtained by MAML can not be compared directory to SAC's result. Hence, we implement REINFORCE( which is also a subclass of on-policy) multiple-agents as another baseline.

1. Implement a MAML multiple-agents class (Young's work)
   * [Reference repositories](https://github.com/shunzh/pytorch-maml-rl)
   * It might takes a month to implement
2. Implement a REINFORCE multiple-agents class (30 hours)

   * I wrote the code of this class. However, the parameters tuning of the agents hasn't completed.  I tried to tune the parameters to get a better policy. The code is [here](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/10_code/CityLearn_REINFORCE2_agent.ipynb).
   * As a result of tuning, I found it is a little bit worse than the rule-based agent. Some extensions of REINFORCE are proposed, such as A2C and PPO. I'll try those methods to get good baselines.
3. Evaluate how the original SAC multiple-agents class works for a unknow task (Felipe's work)

   * Unknown task: in case that the environment has diffrent types of building.

Young, me, and Filepe will worked individually on task 1, 2, and 3 respectively.

**YZ: Nice work of the summary! I have no further comments about it.**

## Goal: week 8&9 3/8 ~ 3/19

In our storyboad, the current theme is still corresponding to **Theme 1.3**.

> We will start implementing algorithms into city-learn or different simulators and evaluate the performance for each algorithms. 

As one of the comparison methods with MAML, I'll keep implementing REINFORCE agent. As I mentioned in the report, I'll implement A2C and PPO in order. A2C is a subclass of REINFORCE, and it has a critic-network in addition to a policy-network to estimate state-value properly. Also, PPO is an extensional method of A2C, which updates its policy gradually. The main idea is that after an update, the new policy should be not too far from the old policy. For that, PPO uses clipping to avoid too large update.



1. Implement a REINFORCE multiple-agents class (30 hours, due to the next meeting, Mar 15.)

   * implementing A2C

   * implementing PPO (if A2C desn't produce a good policy)

   * evaluate those methods

     * First, using those methods, I train a policy on CityLearn simulator with climate zone 2

       a.  evaluate transfer learning: how trained policy in climate zone works in climate zone 1.
       b.  train the policy in climate zone 1 with default policy weight.
       c.  train the policy in climate zone 1 with the policy weight gotten from a.

       Hopefully, we assume in all cases of a, b, and c, MAML's results are better than mine.


**YZ: 30hrs seems pretty long to me. Hopefully you can find time to do it and not overburden.**
