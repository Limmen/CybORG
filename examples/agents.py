from agents import RedTableWrapper

if __name__ == '__main__':
    path = str(inspect.getfile(Main))
    path = path[:-10] + '/Shared/Scenarios/Scenario2.yaml'

    env = Main(path,'sim')

    agent = B_lineAgent()

    results = env.reset('Red')
    obs = results.observation
    action_space = results.action_space

    for i in range(16):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation

        print(action)

    action = Restore(hostname='Op_Server0',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    action = Restore(hostname='Enterprise2',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    action = Restore(hostname='Enterprise1',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    for i in range(12):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation

        print(action)
        print('Success:',obs['success'])

    agent = RedMeanderAgent()

    results = env.reset('Red')
    obs = results.observation
    action_space = results.action_space

    for i in range(46):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation

        print(action)

    action = Restore(hostname='Op_Server0',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    action = Restore(hostname='Enterprise2',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    action = Restore(hostname='Enterprise1',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    action = Restore(hostname='Enterprise0',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    for i in range(24):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation
        print(env.get_last_action('Red'))

    env = Main(path,'sim',agents={'Red':B_lineAgent})

    agent = BlueReactRemoveAgent()

    results = env.reset('Blue')
    obs = results.observation
    action_space = results.action_space

    for i in range(12):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Blue')
        obs = results.observation
        print(env.get_last_action('Blue'))

    agent = BlueReactRestoreAgent()

    results = env.reset('Blue')
    obs = results.observation
    action_space = results.action_space

    for i in range(12):
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Blue')
        obs = results.observation
        print(env.get_last_action('Blue'))

    agent = GreenAgent()

    results = env.reset('Green')
    obs = results.observation
    action_space = results.action_space

    for i in range(12):
        print(agent.get_action(obs,action_space))

    cyborg = Main(path, 'sim',agents={'Blue':BlueMonitorAgent})
    env = RedTableWrapper(env=cyborg, output_mode='table')

    agent = KeyboardAgent()

    results = env.reset('Red')
    obs = results.observation
    action_space = results.action_space

    for i in range(3):
        print(obs)
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation