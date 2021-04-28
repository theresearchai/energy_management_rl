# Report

This documents reports the achievements of the goals set for the week between February 7th and February 13th.

It comprises a set of goals, all of which stem from Theme 1.3 

The goals were the following:

* Read the seminal paper describing the MAML algorithm and its pseudo-code
* Read the seminal paper describing the PEARL algorithm and its pseudo-code
* Code our own version of MAML algorithm to use with the City Learn simulator
* Evaluate the performance of both MAML and PEARL as a meta-reinforcement learning solution to speed up the learning process

The first two goals were achieved. Each member of the group individually read both the MAML and the PEARL seminal papers.

Concerning our 3rd goal, our client expressed, in our weekly meeting, we should not pursue it. There was possibly some communication issue here, as we had already discussed it in our meeting the previous week (and hence it became officially a goal), but in this meeting he expressed he didn't believe it was a good idea. Rather, we should look for another package. I must say I agree with him that this is a better approach. The bottom line is that the 3rd goal was reformulated to become one of next week's goals:  to find another package to do Meta-Reinforcement Learning within the *City Learn* environment.

As for the 4th goal, attempts to use MAML and PEARL from within the _City Learn_ framework have failed, but raised our awareness to a very important fact: we have not been able to reproduce _City Learn's_ results for the centralized agent problem (i.e. a single agent managing multiple buildings). In a previous meeting with _City Learn's_ creator himself, he acknowledged his own uncertainties regarding the centralized agent problem in _City Learn_. By failing to reproduce _City Learn's_ results, we have no benchmark to use to debug our own code. This is a very important finding, as it underscores a significant decision we had to take, namely, to change the problem we're attempting to address in this project. Likewise, it acts as the _raison d'être_ for next week's goals. Of course, there is more context to this but, to avoid redundancy, I will not go into the details here, but will rather provide such context on the document where I set next week's goals.

  