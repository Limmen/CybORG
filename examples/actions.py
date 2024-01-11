import random
import inspect
from csle_cyborg.agents.simple_agents.b_line import B_lineAgent
from csle_cyborg.shared.actions.abstract_actions.discover_network_services import DiscoverNetworkServices
from csle_cyborg.shared.actions.abstract_actions.discover_remote_systems import DiscoverRemoteSystems
from csle_cyborg.shared.actions.abstract_actions.exploit_remote_service import ExploitRemoteService
from csle_cyborg.shared.actions.abstract_actions.analyse import Analyse
from csle_cyborg.shared.actions.abstract_actions.remove import Remove
from csle_cyborg.shared.actions.abstract_actions.restore import Restore
from csle_cyborg.shared.actions.abstract_actions.privilege_escalate import PrivilegeEscalate
from csle_cyborg.shared.actions.action import Sleep
from csle_cyborg.main import Main
from pprint import pprint

if __name__ == '__main__':
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/shared/scenarios/Scenario2.yaml'
    env = Main(path, 'sim')
    results = env.reset(agent='Red')
    action_space = results.action_space
    pprint(action_space.keys())
    actions = action_space['action']
    pprint(actions)
    ips = action_space['ip_address']
    pprint(ips)
    unknown_ips = [ip for ip in ips if not ips[ip]]
    ip = random.choice(unknown_ips)
    action = DiscoverNetworkServices(session=0,agent='Red',ip_address=ip)
    results = env.step(action=action,agent='Red')
    print(results.observation)
    pprint([action.__name__ for action in actions if actions[action]])
    action = Sleep()
    results = env.step(action=action,agent='Red')
    print(results.observation)
    subnets = action_space['subnet']
    known_subnets = [subnet for subnet in subnets if subnets[subnet]]
    subnet = known_subnets[0]
    action = DiscoverRemoteSystems(subnet = subnet, session=0,agent='Red')
    results = env.step(action=action,agent='Red')
    pprint(results.observation)
    known_ips = [ip for ip in ips if ips[ip]]
    ip = random.choice(known_ips)
    action = DiscoverNetworkServices(ip_address=ip,session=0,agent='Red')
    results = env.step(action=action,agent='Red')
    pprint(results.observation)
    action = ExploitRemoteService(ip_address=ip,session=0,agent='Red')
    results = env.step(action=action,agent='Red')
    pprint(results.observation)
    hostname = results.observation[str(ip)]['System info']['Hostname']
    action = PrivilegeEscalate(hostname=hostname,session=0,agent='Red')
    results = env.step(action=action,agent='Red')
    pprint(results.observation)
    results = env.reset(agent='Red')
    obs = results.observation
    action_space = results.action_space
    agent = B_lineAgent()

    while True:
        action = agent.get_action(obs,action_space)
        results = env.step(action=action,agent='Red')
        obs = results.observation

        if action.__class__.__name__ == 'Impact':
            print(action)
            print(obs)
            break
    env = Main(path, 'sim',agents={'Red':B_lineAgent})
    results = env.reset('Blue')
    actions = results.action_space['action']
    pprint([action.__name__ for action in actions if actions[action]])
    action = Sleep()
    for i in range(4):
        results = env.step(action=action,agent='Blue')
        obs = results.observation
        if i == 2:
            # The particular obs we want
            pprint(obs)
    action = Analyse(hostname='User1',session=0,agent='Blue')

    for i in range(2):
        results = env.step(action=action,agent='Blue')
        obs = results.observation
        if i == 1:
            pprint(obs)
    action = Remove(hostname='Enterprise1', session=0, agent='Blue')

    for i in range(2):
        results = env.step(action=action,agent='Blue')
        obs = results.observation
        pprint(obs)
        print(73*'-')
        print(env.get_last_action('Red'))
        print(73*'*')
    for i in range(10):
        env.step() # So Red's actions don't interfere

    action = Analyse(hostname='User1', session=0, agent='Blue')
    results = env.step(action=action,agent='Blue')
    obs = results.observation
    pprint(obs)

    action = Restore(hostname='User1', session=0, agent='Blue')
    results = env.step(action=action,agent='Blue')
    obs = results.observation
    pprint(obs)

    action = Analyse(hostname='User1', session=0, agent='Blue')
    obs = results.observation
    pprint(obs)

    action = Analyse(hostname = "Uncle Ted's Macbook", session = 1.1, agent='Cyan')

    results = env.step(action=action,agent='Blue')

    print(results.action)
    print(results.reward)