# Weekly Report

This report addresses the accomplishments of the goals set out for the week from January, 30th to February 6th.

We have been studying Meta Reinforcement Learning as an approach to increase the learning speed of our algorithm. With this in mind, two weeks ago, we had set for ourselves the following goals:

1. To study and to learn about Meta-Learning, from general concepts to the specifics of the MAML and PEARL approaches;
2. To experiment with the _garage_ package in Python, that allows you to implement MAML and PEARL meta-reinforcement learning algorithms;
3. After completing goals 1 and 2, to figure out how we could use "MAML/PEARL + Garage"  to accelerate the learning process, thus tying up these goals with Theme 1.3.

Concerning whether we had accomplished the first goal, I wrote the following paragraph in the previous report:

> The **first goal** (to study and to learn about Meta-Learning, from general concepts to the specifics of the MAML and PEARL approaches) was accomplished. We have decided not to move on with the PEARL approach, but rather to pursue exclusively with the MAML approach. The reason for this is that MAML is a less complex approach to Meta-Reinforcement Learning, therefore being easier and faster to train. Besides, if Meta-Reinforcement Learning proves of little value, MAML will tell us that before PEARL does. Moreover, for the sake of Theme 1.4 (publishing our findings in a journal), MAML is sufficiently a state-of-the-art technique. Hence, after accomplishing our first goal, our understanding is that we should proceed with Meta-Reinforcement Learning, but that we should focus on the MAML algorithm, and not pursue any endeavors with the PEARL algorithm.

In this week's meeting, however, our client told me that I had misunderstood, and that he expects us to implement _both_ MAML and PEARL algorithms. The reason he gave me was that, in reality, while MAML would be easier and faster to train, PEARL wouldn't be any harder to _implement_ using the _garage_ package, and it might lead to a better performance. I expressed my view that, even though it may MAML and PEARL may both require the same effort to implement, implementing both algorithms would still require double the amount of time than coding a single algorithm, and our MIDS deadline is approaching quickly. So he told us it wouldn't be a major problem if we could not implement both algorithms, but we should set it as our goal. Hence, this week's goals will reflect the return of implementing PEARL as one of our endeavors.

Another important event that should reported is that we will not be using the _garage_ package any longer. Upon closer inspection of this package, we found that it does not integrate well with the City Learn simulator. Creating such integration ourselves would be very time consuming. So much that we decided it would be best to code our own MAML and PEARL algorithms from scratch. 

As a result, all the goals we set for ourselves the previous week have been postponed, namely:

* study the different kinds of buildings available at the CityLearn simulator;
* analyze how to generate data for each kind of building;
* collect this data and explore its applications as an input to the MAML meta-reinforcement learning algorithm

Neither of these are of concern for us right now. Rather, our accomplishments this week have been to realize that the _garage_ package cannot be integrated to City Learn in any practically feasible way, so we'll need to change the direction of our project was heading in order to build our own tools. Namely, we'll have to build our own code to do MAML and PEARL, and this takes precedence over every goal we had expected to dive into this week.

**Comments from YZ: Thanks for putting such a thorough summary for last week's work progress. I do not have further comments. I will keep on joining your weekly meeting with the clients. **



