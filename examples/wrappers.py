import inspect
from cyborg import Main
from agents import B_lineAgent
from pprint import pprint

if __name__ == '__main__':
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/Shared/Scenarios/Scenario2.yaml'
    cyborg = Main(path,'sim')

    env = EnumActionWrapper(cyborg)
    results = env.reset(agent='Blue')
    action_space = results.action_space
    print('Blue action space:',action_space)
    results = env.reset(agent='Red')
    action_space = results.action_space
    print('Red action space:', action_space)
    env = FixedFlatWrapper(Main(path, 'sim'))
    results = env.reset()
    obs = results.observation
    print(type(obs))
    print(len(obs))
    wrappers = FixedFlatWrapper(EnumActionWrapper(cyborg))
    env = OpenAIGymWrapper(env=wrappers,agent_name='Blue')

    obs = env.reset()
    print('Observation:',obs)
    print(73*'-')
    print('Action_Space:',env.action_space)
    print(73*'-')
    print('Observation Space:',env.observation_space)

    env = TrueTableWrapper(cyborg)
    env.reset()
    true_table = env.get_agent_state('True')
    print(true_table)
    cyborg = Main(path,'sim', agents={'Red':B_lineAgent})

    env = BlueTableWrapper(cyborg)

    results = env.reset(agent='Blue')

    for i in range(3):
        results = env.step(agent='Blue')
        blue_obs = results.observation
        print(blue_obs)

    env = BlueTableWrapper(cyborg,output_mode='vector')

    env.reset(agent='Blue')
    for i in range(3):
        results = env.step(agent='Blue')
        blue_obs = results.observation
        print(blue_obs)
        print(76*'-')

    env = RedTableWrapper(cyborg)

    results = env.reset(agent='Red')
    print(results.observation)

    for i in range(3):
        results = env.step(agent='Red')
        red_obs = results.observation
        print(red_obs)

    env = ChallengeWrapper(env=cyborg,agent_name='Red')

    obs = env.reset()

    for i in range(1):
        obs, reward, done, info = env.step()
        print(obs)
        print(76*'-')
        print(reward)
        print(76*'-')
        print(done)
        print(76*'-')
        pprint(info)