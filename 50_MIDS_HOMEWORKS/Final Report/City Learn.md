City Learn [@Vazquez-Canteli2019] is a simulation environment for energy demand response. In its simplest form, it considers a generator (that supplies energy) and a building (that consumes energy). Demand for energy varies according to time zone and time of day. The building can stock energy during periods of low-demand to use during periods of high-demand, but there's a limit to how much energy the building can stock. The building seeks to minimize a cost function which considers a series of factors: amount spent on energy, risk of shortage, risk of rampage, and others.

In a not-so-simple scenario, there are multiple generators and multiple buildings. An agent decides how much energy should be used by or stocked at each building, so as to minimize the cost function for the *network* (not any individual building). There are various different types of energy that can be considered, such as thermal energy, batteries, and air-to-water heat pumps. While they can all be stocked, they do have different prices.

To be more specific, City Learn simulates an environment where a set of $N$ buildings are, at any given time $t$, in a state that is completely defined by 28 variables. These variables are of the following types:

- Temporal variables as “month”, “day”, or “hour”
- Temperature variables
- Humidity variables
- Diffuse solar radiation variables
- Storage variables(How much energy is stored)

We find it important to highlight that all but the last type of variable are related to the demand of energy. Indeed, the demand for energy varies through time depending on temperature , humidity or the speed with which energy dissipates. The last kind of variable, however, refers to storage. And storage is ultimately a "managerial" decision: it's how the agent choses to manage the network. Such choice has implications that deserve our attention: If a building stocks energy today, it is betting that energy today will be cheaper than in the future. Moreover, if it choses to use energy it has previously stocked, it is limited by the choice of how much it decided to stock in the past. Hence, the storage variables insert a path dependency into our problem.

As for the actions, there are only 2 actions possible for the agent to take

- Increasing or decreasing the energy in cooling storage
- Increasing or decreasing the energy in domestic hot water storage

Since each building has its own storage, such 2 actions are, in reality, 2 actions *per building*. In other words, the agent must decide how much energy will de put in storage (or taken out of storage) for each building.

Such agent may be a single agent, managing the entire network, or a set of agents, one responsible for each building, which act independently but can communicate with each other.

