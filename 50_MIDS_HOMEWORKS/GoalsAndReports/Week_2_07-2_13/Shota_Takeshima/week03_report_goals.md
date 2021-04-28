Shota Takeshima: In this document, I write the report of what I have done this week, and mention the goal next week. **Based on the feedback of last week's report and goal, I add the time I spent to complete each task, my working pace, and links to my works in git repository.**

## Report: week 3 1/30 ~ 2/5

In our storyboad, the current theme is still corresponding to **Theme 1.3**.

> We will start implementing algorithms into city-learn or different simulators and evaluate the performance for each algorithms. 

At the meeting with the client on Feb 1, the client suggested us to create MAML or PEARL algorithm on CityLearn simulator. First, we focused on only MAML algorithm. However, considering its training performance and its necessary amount of data (observations from the interaction between RI agent and the simulator) to achieve accuracy, one of the other RI algorithms, PEALRL, is also helpful to solve our problem by combinational use of MAML and it. Also, to implement MAML, first, we planned to use `garage` package that includes many RI algorithms, such as MAML and TRPO. Because of CityLearn's bugs and unclearness of the `garage` document, we thought it was hard to incorporate the CityLearn simulator into `garage` meta-learning framework. However, later last week I managed to incorporate CityLearn to `garage` and confirm the framework works. It still has a problem that I can not get the optimal policy that produces an acceptable future return. So, in the meeting on Feb 8, we'll discuss whether we keep using `garage` or create our own MAML algorithm without `garage`.

1. to incorporate CityLean Simulator to Garage meta-learning framework: 

   This took 18 hours to complete, the pace is on schedule. 

   * First, I needed to get used to `garage`. So, referring to its document, I tried to create a simple RI agent example with OpenAI gym cart pole simulator. (File is here:[playing_with_garage.ipynb](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/10_code/playing_with_garage.ipynb))
   * Next, I tried to incorporate CityLearn simulator into `garage`. It worked without error but still has a problem that the policy cannot be improved well. I guess `garage` is a more academic tool unlike other RI package (`stable baselines 3`) and there are a lot of parameters we need to designate. To achieve acceptable policy, we should investigate algorithms themselves, how functions and parameters in `garage` mean deeply. (File is here:[CityLearn_with_garage.ipynb](https://gitlab.oit.duke.edu/duke-mids/workingprojectrepositories/2020-2021/power-grid/-/blob/master/10_code/CityLearn_with_garage.ipynb))

2. to read [the original paper of MAML](https://arxiv.org/abs/1910.10897)

   This took 3 hours to complete, the pace is on schedule. 

   * This was my individual agenda. To understand MAML algorithm deeper.

   * MAML works based on a policy gradient approach. In the meta-training stage, instead of optimizing policy parameters for one task, it takes samples from several tasks. It optimizes policy parameters averagely (rigorously saying, a weighted average based on the distribution of tasks ). In the meta-testing stage, we can get an optimal policy by tuning the parameters of the trained policy a little bit for a target environment.

**Comments from YZ: Good job summarying the reports. I have no further comments related with it.**



## Goals: week 4 2/8 ~ 2/12

This week we are still in **Theme 1.3**. As mentioned above, at this week's meeting on Feb 8, we need to determine how we implement MAML with CityLearn. One possible way is using `garage`. Another is creating MAML or PEARL algorithm by ourselves. In both cases, we first try to train a RI agent and evaluate on a simple case that the environment has only one building (one type). Then we observe how the trained agent performs on another building (another type of building). Then (week 5 ~ ), we'll expand the case that the environment has multiple buildings. All tasks below are for individuals. But if necessary, we divide the task into subtasks and assign them to members.

1. Create MAML algorithm and evaluate the agent trained by it on a simple environment (~ Feb 11)
   * How we implement MAML depends on the next meeting
2. to read the original paper of MAML and PEARL (~ Feb 8 13:30 before meeting)
   * Either way, using `garage` or creating by ourselves, we need to know how those algorithms work and how to tune their parameters.
   * Fortunately, in the previous week, I've already read the paper of MAML. So, I'll focus on reading PEARL and investigating its implementation.

**Comments from YZ: Good job in specifying the two tasks. The only question I have is how you plan to assign your time to task 1, and what kind of obstacles in creating the algorithm? Also could you be more specific on you plan to team work for this week? I think this is one of the missing points in your group goals. **
