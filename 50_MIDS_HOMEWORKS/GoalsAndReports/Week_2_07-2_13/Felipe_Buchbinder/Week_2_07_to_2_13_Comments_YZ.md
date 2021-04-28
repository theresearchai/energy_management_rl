# Goals

This documents states the goals for the week between February 7th and February 13th.

It comprises a set of goals, all of which stem from Theme 1.3 

In our previous goals and reports, we mentioned we were going to implement Meta-Reinforcement Learning as a means to speed up the learning process. There are two approaches to Meta-Reinforcement Learning, one called MAML and the other called PEARL. My understanding had been that we would endeavor to implement MAML, as there seemed to be little to gain by implementing two approaches to address the same problem. That was my understanding. It seems, however, that I misunderstood, and that our client does want us to implement both algorithms. 

With this in mind, we should add the following goal:

* Evaluate the performance of both MAML and PEARL as a meta-reinforcement learning solution to speed up the learning process

Upon evaluating the use of the _garage_ package to implement MAML and PEARL, it became evident that the _garage_ package will not integrate well with the _City Learn_ simulator. The effort to create this integration would be too high. A more feasible solution is to code our own version of the MAML and PEARL algorithms from scratch. So this yields our next two goals:

* Read the seminal paper describing the MAML algorithm and its pseudo-code
* Code our own version of MAML algorithm to use with the City Learn simulator

For a matter of fact, we will also have to code our own version of a PEARL algorithm, but I don't put it as a goal at this moment, because it's not something we're aiming to accomplish this week. However, at least the first part of this future goal, namely, reading the paper, is already due this week:

* Read the seminal paper describing the PEARL algorithm and its pseudo-code

It is worth mentioning that goal to code our own version of the MAML algorithm is initially focused on applying it to City Learn's single agent problem. This is because applying it to the single agent problem is likely easier than applying it to the multi-agent problem. Our client, however, is interested in the multi-agent problem, and has anticipated that the generalization from the single-agent case to the multi-agent case is something we will be dealing with in the upcoming weeks. Yet, I merely mention this, without enshrining it as a goal, because it is not a goal for this week, but rather more long(ish)-term planning.

**Comments from YZ: Good work in putting details for your goals. I want you to stretch your thinking a little bit, by incorporating: will these goals include teamwork, or will be finished individually? If it is teamwork, how do you plan to work among with the other two members? How long you expect to spend for each goal? **
