import inspect
from CybORG.main import Main
from CybORG.Agents.SimpleAgents.Meander import RedMeanderAgent
from CybORG.Agents.Wrappers.BlueTableWrapper import BlueTableWrapper
from CybORG.Agents.Wrappers.EnumActionWrapper import EnumActionWrapper
from CybORG.Agents.Wrappers.OpenAIGymWrapper import OpenAIGymWrapper
from CybORG.Agents.Wrappers.ReduceActionSpaceWrapper import ReduceActionSpaceWrapper


def run():
    path = str(inspect.getfile(Main))
    path = path[:-10] + '/Shared/Scenarios/Scenario1b.yaml'
    red_agent = RedMeanderAgent
    agent_name = 'Red'
    c = OpenAIGymWrapper(agent_name,
                              EnumActionWrapper(
                                  ReduceActionSpaceWrapper(
                                      BlueTableWrapper(
                                          Main(path, 'sim', agents={'Red': red_agent}),
                                          output_mode='vector'))))
    for i in range(100):
        for i in range(50):
            c.step()
        c.reset()

# cProfile.run("run()", sort='cumtime')
run()

#cyborg = DummyVecEnv([lambda: cyborg])
# num_cpu = 4
# cyborg = SubprocVecEnv([make_blue_env(red_agent) for i in range(num_cpu)])
