Shota Takeshima: In this document, I write the report of what I have done this week, and mention the goal next week. **Based on the feedback of last week's report and goal, I add comments on how you and your group work together to work on this tasks..**

## Report: week 5 2/15 ~ 2/19

This week we are still in **Theme 1.3**. As mentioned above, this week, first, we'll decide which package is used for our implementation or referred to at our weekly meeting on Feb 15. Now, I think there are two options to implement MAML on Citylearn. One is to create our own multiple agents by ourselves. In this case, we need to write MAML code, referring to the git repository we found last week. In this case, we can use information sharing in MAML. Another is to remove dependencies between agents and make them independent. In this case, we can use the MAML package for single-agent directly. However, not using information sharing might worsen the result. After determining how we implement MAML, we started to implement. 

1. Create pseudo-code to implement MAML algorith (10h)
   * Young mainly consider the pseudo-code to implement MAML algorithm on CityLearn. [Here](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/40_docs/psuedocode.pdf) is the memo of the pseudo-code.
   * I also checked the psedo-code and confirmed it matches the algorithm in [the original paper](https://arxiv.org/abs/1703.03400).
2. Divide the implementation task into sub tasks(10h)
   * We plan to modify the SAC multiple-agents class that is included in the CityLearn package to our MAML multiple-agents class.
   * This week, because the SAC multiple-agents class includes unnecessary parts to implement MAML, we did code reading and review. After that, I removed the unnecessary parts from it and implemented REINFORCE multiple-agents class.
     * REINFORCE and MAML are subsets of policy gradient methods. REINFORCE is easier to implement compared to MAML. So, to get used to the implementation and create a template of the MAML multiple-agents class, I wrote the code. [Here](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/10_code/CityLearn_REINFORCE_agent.ipynb) is my code.

**Comments by YZ: Good summary. I have no further questions about your report.**

## Report: week 6 2/22 ~ 2/26

In our storyboad, the current theme is still corresponding to **Theme 1.3**.

> We will start implementing algorithms into city-learn or different simulators and evaluate the performance for each algorithms. 

After checking some MAML repository, we decided to implement our MAML multiple-agents class, referring to those repositories. As I mentioned above in the report, we organized and cleaned up the source code of the original multiple-agents class (SAC multiple-agents class). Using this as a template, we'll implement a MAML multiple-agents class and evaluate it. Thinking about the evaluation, the comparison baselines are needed. The first one is the SAC multiple-agents included in CityLean. The benefit of MAML is that we can get a good policy for an unknown task after training for a short duration. We confirm how the original SAC multiple-agents work against the unknown task (different types of buildings) for a short training. (Hopefully, we want to get a bad result.) Another baseline is REINFORCE multiple-agents. There are two main types of reinforcement learning algorithms, such as on-policy and off-policy approaches. SAC is a subclass of the off-policy, and MAM is a subclass of on-policy. So, although it depends on the problem, there is a possibility that the result obtained by MAML can not be compared directory to SAC's result. Hence, we implement REINFORCE( which is also a subclass of on-policy) multiple-agents as another baseline.

1. Implement a MAML multiple-agents class

   * [Reference repositories](https://github.com/shunzh/pytorch-maml-rl)

   * It might takes a month to implement

2. Implement a REINFORCE multiple-agents class (20 hours, due to the next meeting, Mar 1.)

   * As I mentioned in the report, I wrote the code of this class. However, the parameters tuning of the agents hasn't completed. So, this week, I'll try to tune the parameters to get a better policy.
   * REINFORCE algorithm I implemented is very simple one. The extension of REINFORCE is proposed. So, if the tuning doesn't work well, I'll implement more advanced REINFORCE.

3. Evaluate how the original SAC multiple-agents class works for a unknow task

   * Unknown task: in case that the environment has diffrent types of building.

Young, me, and Filepe will work individually on task 1, 2, and 3 respectively.

**Comments by YZ: It should be the "goal" of the following two weeks, not "reports". **




