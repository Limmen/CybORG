# Copyright DST Group. Licensed under the MIT license.

# Cyber Operations Research Gym (CybORG)

A cyber security research environment for training and development of security human and autonomous agents. Contains a common interface for both emulated, using cloud based virtual machines, and simulated network environments.

## Installation

Install CybORG locally using pip

```
# from the cage-challenge-2/CybORG directory
pip install -e .
```


## Creating the environment
Create a CybORG environment with:
```
from CybORG import CybORG
path = str(inspect.getfile(CybORG))
path = path[:-7] + '/Shared/Scenarios/Scenario2.yaml'
cyborg = CybORG(path, 'sim')
```

 


To create an environment where the red agent has preexisting knowledge of the network and attempts to beeline to the Operational Server use:

 

```
red_agent = B_lineAgent
cyborg = CybORG(path, 'sim', agents={'Red': red_agent})
```
To create an environment where the red agent meanders through the network and attempts to take control of all hosts in the network use:

 

```
red_agent = RedMeanderAgent
cyborg = CybORG(path, 'sim', agents={'Red': red_agent})
```
To create an environment where the red agent always takes the sleep action use:
```
red_agent = SleepAgent
cyborg = CybORG(path, 'sim', agents={'Red': red_agent})
```

 

## Wrappers

 

To alter the interface with CybORG, [wrappers](cyborg/agents/Wrappers) are avaliable.

 

* [OpenAIGymWrapper](cyborg/agents/Wrappers/OpenAIGymWrapper.py) - alters the interface to conform to the OpenAI Gym specification.
* [FixedFlatWrapper](cyborg/agents/Wrappers/FixedFlatWrapper.py) - converts the observation from a dictionary format into a fixed size 1-dimensional vector of floats
* [EnumActionWrapper](cyborg/agents/Wrappers/EnumActionWrapper.py) - converts the action space into a single integer
* [IntListToActionWrapper](cyborg/agents/Wrappers/IntListToAction.py) - converts the action classes and parameters into a list of integers
* [ReduceActionSpaceWrapper](cyborg/agents/Wrappers/ReduceActionSpaceWrapper.py) - removes parameters from the action space that are unused by any of the action classes
* [BlueTableWrapper](cyborg/agents/Wrappers/BlueTableWrapper.py) - aggregates information from observations and converts into a 1-dimensional vector of integers

 


## Evaluating agent performance

 

To evaluate an agent's performance please use the [evaluation script](cyborg/evaluation/evaluation.py). 

 


The [wrap function](cyborg/evaluation/evaluation.py#L22-L23) defines what wrappers will be used during evaluation.
```
def wrap(env):
    return ChallengeWrapper(env=env, agent_name='Blue')
```
The agent under evaluation is defined [here](cyborg/evaluation/evaluation.py#L42-L43). 
To evaluate an agent, extend the [BaseAgent](cyborg/agents/SimpleAgents/BaseAgent.py). 
We have included the [BlueLoadAgent](cyborg/agents/SimpleAgents/BlueLoadAgent.py) as an example of an agent that uses the stable_baselines3 library.
```
# Change this line to load your agent
agent = BlueLoadAgent()
```

## Additional Readings
For further guidance on the CybORG environment please refer to the [tutorial notebook series.](cyborg/tutorial)

## Citing this project
```
@misc{cage_challenge_2,
  Title = {Cyber Autonomy Gym for Experimentation Challenge 2},
  Note = {Created by Maxwell Standen, David Bowman, Son Hoang, Toby Richer, Martin Lucas, Richard Van Tassel, Phillip Vu, Mitchell Kiely},
  Publisher = {GitHub},
  Howpublished = {\url{https://github.com/cage-challenge/cage-challenge-2}},
  Year = {2022}
}
```

## DSTG Development team 

* **David Bowman** - david.bowman@dst.defence.gov.au
* **Martin Lucas** - martin.lucas@dst.defence.gov.au
* **Toby Richer** - toby.richer@dst.defence.gov.au
* **Maxwell Standen** - max.standen@dst.defence.gov.au
