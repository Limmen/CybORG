import inspect
import random
from pprint import pprint
from cyborg import Main
from agents import B_lineAgent
from shared.Actions import Analyse

if __name__ == '__main__':
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/Shared/Scenarios/Scenario2.yaml'

    env = Main(path, 'sim')

    results = env.reset(agent='Red')
    obs = results.observation
    pprint(obs)
    pprint(obs['User0'])
    blue_obs = env.get_observation('Blue')

    print(list(blue_obs.keys()))
    pprint(blue_obs['User0'])
    action_space = results.action_space
    red_obs = results.observation
    agent = B_lineAgent()

    def step_red(obs):
        action = agent.get_action(obs,action_space)
        print('Red Action:',action)
        print(76*'-')

        results = env.step(action=action,agent='Red')
        obs = results.observation
        pprint(obs)

        return results

    results = step_red(red_obs)
    red_obs = results.observation
    print(env.get_observation('Blue'))
    results = step_red(red_obs)
    red_obs = results.observation

    blue_obs = env.get_observation('Blue')
    print(76*'-')
    print('Blue Observation:')
    print(76*'.')
    pprint(blue_obs)
    print(76*'.')
    random.seed(1) # Guarantee Red can be detected when block first executed

    results = step_red(red_obs)
    red_obs = results.observation


    blue_obs = env.get_observation('Blue')
    print(76*'-')
    print('Blue Observation:')
    print(76*'.')
    pprint(blue_obs)

    random.seed(0) # Guarantee Red invisible when block first executed

    results = step_red(red_obs)
    red_obs = results.observation

    blue_obs = env.get_observation('Blue')
    print(76*'-')
    print('Blue Observation:')
    print(76*'.')
    pprint(blue_obs)

    results = step_red(red_obs)
    red_obs = results.observation

    blue_obs = env.get_observation('Blue')
    print(76*'-')
    print('Blue Observation:')
    print(76*'.')
    pprint(blue_obs)

    action = Analyse(session=0,agent='Blue',hostname='User1')
    results = env.step(action=action,agent='Blue')
    pprint(results.observation)