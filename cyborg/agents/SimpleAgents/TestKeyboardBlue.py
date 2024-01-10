from cyborg.main import Main
import inspect
from cyborg.agents.SimpleAgents.KeyboardAgent import KeyboardAgent
from cyborg.agents.SimpleAgents.GreenAgent import GreenAgent
from cyborg.agents.SimpleAgents.B_line import B_lineAgent
from cyborg.agents.Wrappers.BlueTableWrapper import BlueTableWrapper


if __name__ == "__main__":
    print("Setup")
    path = str(inspect.getfile(Main))
    path = path[:-7] + '/Shared/Scenarios/Scenario1b.yaml'

    agents = {'Red': B_lineAgent,'Green': GreenAgent}
    # agents = {'Red': RedMeanderAgent,'Green': GreenAgent}
    cyborg = BlueTableWrapper(Main(path, 'sim',agents=agents), output_mode='table')
    
    agent_name = 'Blue'

    results = cyborg.reset(agent=agent_name)
    observation = results.observation
    action_space = results.action_space

    agent = KeyboardAgent()

    reward = 0
    done = False
    while True:
        action = agent.get_action(observation, action_space)
        results = cyborg.step(agent=agent_name, action=action)
        print(cyborg.get_last_action(agent='Red'))
        print('>>> Reward: ', results.reward)

        reward += results.reward
        observation = results.observation
        action_space = results.action_space
        if done:
            print(f"Game Over. Total reward: {reward}")
            break
