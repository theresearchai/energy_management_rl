# Goals 

All goals from this week build on top of Theme 1.3.

In the previous weeks, we have been attempting to use Meta-Reinforcement Learning techniques to speed up the learning process of our agent. The Meta-Reinforcement Learning algorithms we are using are coded in a package called _Garage_. The power grid we are simulating, on the other hand, is offered by a package called _City Learn_. We want to use the meta-reinforcement learning functions offered by the _Garage_ package within the _City Learn_ simulator. However, we have faced big challenges to integrate _Garage_ and _City Learn_. 

We have essentially three options to tackle this problem: (1) either we modify _Garage_ to suit _City Learn_; or we (2) modify _City Learn_ to suit _Garage_; or we (3) do not use _Garage_ whatsoever. The third option could either mean that we would (3a) look for another package to use _in lieu_ of _Garage_, or (3b) code our own version of the _Garage_ package from scratch.

Upon considering the pros and cons of each alternative, we had decided to go with option (3b) i.e. coding our own version of the _Garage_ package from scratch. Indeed, this even figured as one of our goals in last week's report, where I wrote:

> * Code our own version of MAML algorithm to use with the City Learn simulator
>

During this week's meeting, however, our client told us not to embark on such goal, but rather to research another package to use _in lieu_ of Garage. This leads us to our first goal this week:

* Find a package to enable us to do Meta-Reinforcement Learning within the City Learn environment

Once we chose a package, we are to stick to it, and not change it, lest we do not have enough time to deliver our project.

Ok, let's take a step back and discuss something else.

Before deciding to look for another package, we did attempt to tailor the _Garage_ package to suit the _City Learn_ environment. When doing so, we noticed a challenge that may well appear with whichever other package we chose to use. Ultimately, it comes down to the following question: How can we verify that our integration of *CityLearn* and Garage is giving adequate results? 

The answer to this question is that we need a benchmark: a problem whose correct answer is known, so that we can compare the performance of our agent with the known-to-be-correct answer. However, we have been unable to reproduce the results of _City Learn_ when running their code for a central agent on 9 buildings. This suggests there is an issue in *City Learn* itself.

Indeed, on a previous meeting with the author of the *City Learn* package, he told us himself to stay away from the centralized agent modality. On this occasion, we did not follow his advice, because the case of a centralized agent managing multiple buildings is precisely the case we are most interested in. However, failing to reproduce the results from *City Learn* and, thereby, lacking any benchmark to attest the adequate functioning of our code, is just too serious an issue to be neglected. 

Therefore, we will abandon our attempts to model a centralized agent managing multiple buildings, and embrace instead the challenge of modelling a series of decentralized agents managing the same set of 9 buildings. Concerning this alternative problem of decentralized agency, results are documented in published papers, so in all likelihood we should be able to reproduce them and they can be used as the benchmark we are in need of. 

This will require, however, that we delve into the inner workings of how _City Learn_ implements the decentralized agent problem. So far, we haven't really dived deep into this problem, because we were interested in the single agent case. However, now that we are going to focus on the decentralized agent problem, we must understand in detail how it is implemented in *City Learn*. This leads us to our next goal:

* Understand how the decentralized agents problem is implemented in *City Learn*.

Note this will help us better fulfill our previous goal, since a better understanding of the inner workings of *City Learn* can help us best identify which package will integrate well with it.

Another point worth mentioning is that changing the problem is not a decision that comes without theoretical implications. If we have a centralized agent, this one agent has all the information available of all buildings. If, however, each building is managed by its own agent, do they share information? The problem where information is shared is substantially different from a problem where information sharing is absent. This implication is not only theoretically relevant, it also has coding implications:

Training multiple agents in *City Learn* requires looping over multiple buildings. To the best of our knowledge, these loops occur independently, which means that there is no information sharing between buildings. We will attempt a similar solution in whichever package we pick to substitute _Garage_, thereby training all agents independently of each other. In this scenario, there is no information sharing. Once this is established,  we will attempt to include information sharing among agents. These are likely to become goals for the upcoming week or two.

Comments from YZ: I appreciate you put such thorough details for your goals. Again, do you plan to work on these goals individually, or among groups? Is it possible to switch your weekly meeting with the clients from Monday to Friday? It looks to me that the client has been dominating the directions for your weekly goals, and having the meeting on Monday and weekly goals set on Saturday seems not to work very good for your group. 

