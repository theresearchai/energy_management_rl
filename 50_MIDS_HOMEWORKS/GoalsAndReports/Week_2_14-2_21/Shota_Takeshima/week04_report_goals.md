Shota Takeshima: In this document, I write the report of what I have done this week, and mention the goal next week. **Based on the feedback of last week's report and goal, I add the time I spent to complete each task, my working pace, and links to my works in git repository.**

## Report: week 4 2/8 ~ 2/12

In our storyboad, the current theme is still corresponding to **Theme 1.3**.

> We will start implementing algorithms into city-learn or different simulators and evaluate the performance for each algorithms. 

This week we are still in **Theme 1.3**. We need to determine how we implement MAML with CityLearn. One possible way is using `garage`. Another is creating MAML or PEARL algorithm by ourselves. In both cases, we first try to train a RI agent and evaluate on a simple case that the environment has only one building (one type). Then we observe how the trained agent performs on another building (another type of building). Then (week 5 ~ ), we'll expand the case that the environment has multiple buildings. All tasks below are for individuals. But if necessary, we divide the task into subtasks and assign them to members.

1. Create MAML algorithm and evaluate the agent trained by it on a simple environment (12 hours)

   * As a result, we found it is very difficult to use `garage` with CityLearn 
     * Multiple agents (for each buildings) sharing their information works and provide a good result. However, `garage` framework can deal with only single agent.
     * Also, `garage` paskage seems to be used for the academic purpose. Compared to other packages, it required more parameters we designate. Regarding this, it might take a lot of time to investigate the meanings of parameters and algorithms used in it.
   * So, instead of `garage`, we searched another promissing packeage or code we can refer. Also, for CityLearn we think we can not use another packae directly bcause as I said above, multiple agent sharing their information is suitable to CityLearn and most packages can not handle the multiple agents. So, refering the codes, we need to implement algorithm by ourselves.
     * https://github.com/dragen1860/MAML-Pytorch
     * https://github.com/cbfinn/maml_rl

2. to read the original paper of MAML and PEARL  (8 hours)

   * Finished reading those papers

3. Optionally, I also investigated how the results the multiple agents return are different in case we don't use information sharing. (3 hours)

   * Code is [here](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/10_code/replicating_result_CityLearn_MARISA_paper.ipynb)

 **Comments from YZ: Nice summarizing your weekly progress. I do not have further comments.**  

## Goals: week 5 2/15 ~ 2/19

This week we are still in **Theme 1.3**. As mentioned above, this week, first, we'll decide which package is used for our implementation or referred to at our weekly meeting on Feb 15. Now, I think there are two options to implement MAML on Citylearn. One is to create our own multiple agents by ourselves. In this case, we need to write MAML code, referring to the git repository we found last week. In this case, we can use information sharing in MAML. Another is to remove dependencies between agents and make them independent. In this case, we can use the MAML package for single-agent directly. However, not using information sharing might worsen the result. After determining how we implement MAML, we'll start to implement. 

1. Create pseudo-code to implement MAML algorith
2. Divide the implementation task into sub tasks
   * We might create one agent-group class that has multiple policies that control one building included in the environment. In this case, it might be difficult to divide the task and assign part of the task to each team member. So, we might implement in pair programming style. All members create their own agents, but their progress and issues are shared instantly.

**Comments from YZ: It's good that you have very clear goals and tasks for each week. I want to see a little more comments on how you and your group work together to work on this tasks. **
