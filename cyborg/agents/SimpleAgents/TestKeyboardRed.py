from cyborg.main import Main
import inspect
from cyborg.agents.SimpleAgents.BlueMonitorAgent import BlueMonitorAgent
from cyborg.agents.SimpleAgents.KeyboardAgent import KeyboardAgent
from cyborg.agents.Wrappers.RedTableWrapper import RedTableWrapper

if __name__ == "__main__":
    print("Setup")
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/Shared/Scenarios/Scenario1b.yaml'

    cyborg = RedTableWrapper(env=Main(path, 'sim', agents={'Blue': BlueMonitorAgent}), output_mode='table')
    agent_name = 'Red'

    results = cyborg.reset(agent=agent_name)
    observation = results.observation
    action_space = results.action_space

    agent = KeyboardAgent()

    reward = 0
    done = False
    while True:
        action = agent.get_action(observation, action_space)
        results = cyborg.step(agent=agent_name, action=action)

        reward += results.reward
        observation = results.observation
        action_space = results.action_space
        if done:
            print(f"Game Over. Total reward: {reward}")
            break
