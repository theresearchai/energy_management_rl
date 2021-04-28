The task of managing a power grid conforms well to the basic tenants of RL. For each action one takes on a power grid, one has a corresponding consequence to either enjoy or suffer. The grid can have a myriad of different states, the transition probabilities of which are unknown. In short, one must teach an agent which actions to take given only the rewards of such actions. That's the quintessential example of RL [@Lambert2020]. Indeed, there is a vast literature on employing RL to managing power grids (e.g. [@Ademoye2012; @Hadidi2013; @Glavic2017; @Mocanu2019]).

[@Glavic2017] performed a literature review where he analyzed extant challenges and concerns about the employment of RL to power grid management concluding the overall sentiment in the scientific community is that RL is a very promising approach to deal with the task at hand.

Indeed, RL has been employed to multiple problems, all of which fall under the general category of power grid management. Thus, some authors focus on optimizing the generation of electricity ([@Wang2016]), others focus on its distribution ([@Gemine2017]), while others focus on managing the consumption of energy itself ([@Xu2020; @Mocanu2019; @SI2021]). Likewise, some authors focus on controlling the power grid ([@Yousefian2016; @Yousefian2016]), others in stabilizing it ([@Hadidi2013]), while others attempt to modulate demand by setting energy prices dynamically ([@Tsui2012]).

This latter stream of research, in particular, has been receiving a significant share of scholarly attention, and even has a name of its own: demand response. Demand response consists of managing the power grid by modulating the demand for energy. This will typically be done by some sort of price incentive, lowering energy prices when one wishes to increase demand, and raising energy prices when one wishes to decrease it [@Christensen2020; @Kurte2020]. Our paper falls into this category. 

We consider the problem of a small power grid to which buildings of different kinds are connected. The price of electricity varies with time and, in particular, it increases as a response to an unexpected ramping in demand. Buildings use electricity to either heat up or cool down, thereby maintaining a pleasant temperature. The need to heat up or cool down is determined by the outside temperature which varies throughout the year in a way that is specific to the climate zone where the power grid is located. Buildings have the option to store either hot or cold water, that can be used to either heat up or cool down the building at some later time. Hence, if a building is anticipating hot weather on the upcoming days and the price of electricity is cheap at present, it may wish to store cold water, so it can cool itself down when the temperature rises and energy prices are no longer cheap. In making such decisions, however, we assume buildings act independently to each other, with no information sharing between them. All data is simulated, and we use the City Learn package to this end.

Unlike supervised and unsupervised learning, RL often makes use of simulated data (with some exceptions e.g. [@Xu2021]). [@Kang2019] notes that one reason for the ubiquity of simulated data on RL research is because RL requires copious amounts of data, to the extent where getting such data might be very costly, if at all feasible.  [@DeepMind2021] makes an interesting remark on this point. Namely,  [@DeepMind2021] argue that, in some real-world application domains, data may be generated slowly. This is, indeed, the case with our paper. In order to learn how to efficiently manage  energy throughout yearly cycles of succeeding seasons, one would need many years of data. By using simulations, such data can be obtained with no need to wait. 

There is, of course, a trade-off here. While simulated data is much faster and cheaper to obtain in large amounts, it may fail to accurately replicate what real-data would look like. In plain terms, one can always cast doubt on whether a simulator is indeed realistic ([@Dulac2019]). This has led some researchers to endeavor to combine real-data and simulated data ([@Kang2021; @Hanna2019; @Mocanu2019]). 

In spite of such promising developments in the field, there has been a remarkable development in simulators targeted at RL research (e.g. [@DeepMind2021; @OpenAIGym]). At present, most research on RL relies on simulated data. Our paper follows this tradition, and uses the City Learn simulator [@Vazquez-Canteli2019].

The City Learn simulator simulates a small power grid network. As concerns its size, our grid is an intermediate between the one modelled by [@Kuznetsova2013] (which consists of a consumer, a generator and a battery for storage), and the one modelled by [@Yousefian2016] (where dispersion over a large area is a feature that must be considered). In our power grid, there are multiple buildings, but they are sufficiently close together for delays between generation and consumption to be neglected. 

In addition, we have multiple buildings and pay no attention to how is energy distributed inside a building. In this respect, our paper is opposite to that of [@Tsui2012], where one considers a single home but worries about the multiple appliances it contains. 

It is important to highlight, however, that 9 different types of buildings are considered. This should arguably enhance the adherence of our simulated power grid to reality, since in the real-world, there exists buildings with different demands for energy. A commercial building has high demand for electricity during work hours, but a smaller demand during the weekend. The opposite is true for residential buildings.  

Likewise, we consider 4 different clime zones, which means there are 4 distinct ways to simulate how temperature (and hence energy demand) evolves throughout the year. 

In our simulator, buildings can use energy to store either warm or cold water, that will subsequently be used for cooling or heating. Scholars such as [@Tsui2012; and @Xu2020] allow for many more uses of electricity within a building, but their interest lies on a single household. Conversely, scholars such as [@Ademoye2012; and @Mocanu2019] deal with the energy demand as a black box, with no distinction whatsoever as regards its use. Our paper strikes a balance between both approaches: while not delving into all the possible uses of electricity within a building, by allowing two possible uses, it acknowledges that this utility may be used in different ways.

In addition, it's worthy to note that buildings can only store or use energy. They cannot generate energy. In this regard, our approach differs from [@Wang2016], where buildings are equipped with photovoltaic generating systems. This should arguably increase the need for energy storage. While data from the International Energy Agency ([@IEA2020]) suggests global photovoltaic capacity has been doubling every 2.4 years, the same report shows that such capacity is capable of meeting only 3% of the global demand for energy. Hence, at present, it is more realistic to suppose buildings do not have the ability to generate their own energy than to suppose otherwise.

When all such buildings are brought together and integrated into a power grid, one must make the decision as to how such grid is to be managed. One possibility, for example, is to have a single agent decide how each building should act, so as to minimize the cost of managing the entire grid. Such an agent would need to have information on each building's energy needs and storage levels. In its own turn, the agent would combine all this information into a single objective function that considered the costs of all buildings, thus achieving what Economic literature calls the social optimum. [@Yousefian2016] is an example of such an implementation. 

One practical problem of the single agent approach is that granting it information on the energy consumption of each individual building may be perceived as a violation of privacy rights. Moreover, granting control over the power grid to a single agent raises concerns over malpractices such as observed during the California Energy Crisis [@California-Energy-Crisis]. Finally, minimizing the collective cost of energy doesn't necessarily guarantee that each individual building will have its own cost minimized, which may also pose an issue in more individualistic societies. 

Another possibility as to how to manage a power grid is to do precisely the opposite: have each building decide on its own how much energy to use or to store. In plain terms, rather than having a single agent decide what everyone should do, each building shall decide for itself. In this multi-agent approach, each building optimizes its own objective function. In principle, nothing precludes buildings from sharing information among themselves, so it is still possible to incorporate information from multiple buildings within each objective function. Still, since each building optimizes its own objective function (possibly conditioned on its expected behavior of the remaining buildings), there is no guarantee that a social optimum will be achieved. Nonetheless, concerns over privacy, excessive market power and the limitation of the individual's freedom to chose have been greatly reduced. [@Li2012; @Dhamankar2020; @Christensen2020; @Xu2020; and @Ademoye2012] are all examples of this approach.

In our paper, we use a multi-agent approach with no information sharing. This means each building maximizes its own objective function, with no regards whatsoever for other buildings. We chose a multi-agent approach because, in our understanding, it is more realistic, as it evades the caveats cited previously. In addition, by doing so, we align ourselves with the majority of previous research. A third, but equally important reason, results from a meeting we had with the developer of the City Learn simulator, in which he suggested we used the multi-agent approach, since its code is more stable, and has been more tested, than the single agent.

In reality, a hybrid model is often observed, where a large network is broken into regions and, within each region, the generation, transmission and distribution of energy are managed by a single-agent fashion, whereas the buildings are granted autonomy to decide for themselves how much to consume or store. In other words, within a certain region, the decisions pertaining generation, transmission and distribution are made by centralized agents, whereas the actual consumption of energy is made by decentralized agents. The Synchronous grid of Continental Europe [@SGCE], for example, is managed by the European Network of Transmission System Operators for Electricity (ENTSO-E), an organization that is, in turn, comprised by 42 other organizations (called Transmission System Operators, or TSO) that manage the generation, transmission and distribution of electricity within specific regions of the grid. Since the entry costs of generation, transmission and distribution are formidably high, these activities are natural monopolies, so concerns over market power of TSOs cannot be solved by competition. Thus, a single agent approach lends itself naturally to this scenario. The same cannot be said, however, for the demand side of the grid. Hence, as far as buildings are concerned, they are autonomous to make their own decisions regarding energy consumption. Here, what we have is a multiple-agent approach. We have been unable to find any papers that employ such a hybrid model of power grid management. While we acknowledge that such vacuity may be a result of the increased complexity of a hybrid model, we should also point out that this is (to the best of our knowledge) an open field for future research.













jeach building decide on its own what it should do. Each building wil



Conceptually, there are two possibilities: one can either have every building manage itself or, alternatively, assign a single agent to manage the entire system. 







In order to address the issues of whether the simulator is a realistic representation of the real world, 



In our paper, we consider buildings of different types, and in different climate zones. There are 9 kinds of buildings, and 4 kinds of climate zones. In each climate zone



Another reason why simulated data is so often used in RL is that the data itself is not static: it reacts to the actions taken by the agent. So one needs to be able to devise what the data would look like if the agent had followed a different policy. This can be easily done with simulations, but not with a traditional, static, dataset. Finally, simulators offer the opportunity for agents to fail at no cost at all [@Glockner2021], which is particularly relevant for RL algorithms, since they requires multiple iterations before converging to the optimal policy 

Four different climate zones are considered.



Following on the tradition of [@Li2012], [@Dhamankar2020], [@Xu2020] and [@Ademoye2012] -- ma

ademoye -- sim

mocanu 





In our simulator, buildings can use energy to store either warm or cold water, that will subsequently be used for cooling or heating. The fact that energy demand is limited to temperature regulation is not very realistic, as there are many other uses for electricity inside a building, such as illuminating or providing mechanical work. Similarly, one is left to wonder why does the building store warm and  

