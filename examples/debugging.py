import inspect
from pprint import pprint
from cyborg.main import Main
from agents import B_lineAgent
from cyborg.agents.wrappers.true_table_wrapper import true_obs_to_table
from cyborg.shared.actions.abstract_actions.restore import Restore


if __name__ == '__main__':
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/Shared/Scenarios/Scenario2.yaml'
    env = Main(path, 'sim',agents={'Red':B_lineAgent})
    results = env.reset(agent='Blue')
    true_state = env.get_agent_state('True')
    pprint(true_state['User0'])
    print(76*'-')
    true_table = true_obs_to_table(true_state,env)
    print(true_table)
    for i in range(3):
        env.step()
    true_state = env.get_agent_state('True')
    true_table = true_obs_to_table(true_state,env)
    print(env.get_last_action('Red'))
    print(true_table)
    print(76*'-')
    action = Restore(hostname='User1',session=0,agent='Blue')
    env.step(action=action,agent='Blue')

    true_state = env.get_agent_state('True')
    true_table = true_obs_to_table(true_state,env)
    print(true_table)
    env.reset()
    env.step()

    red_obs = env.get_observation('Red')
    pprint(red_obs)

    blue_obs = env.get_observation('Blue')
    pprint(blue_obs)
    print(76*'-')
    red_action = env.get_last_action('Red')
    print(red_action)

    blue_action = env.get_last_action('Blue')
    print(blue_action)
    red_action_space = env.get_action_space('Red')
    print(list(red_action_space))

    blue_action_space = env.get_action_space('Blue')
    print(list(blue_action_space.keys()))
    env.get_ip_map()
    env.get_rewards()
    env.set_seed(100)