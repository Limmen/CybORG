from cyborg.main import Main
import inspect
from cyborg.agents.SimpleAgents.TestAgent import TestAgent
from cyborg.agents.Wrappers.FixedFlatWrapper import FixedFlatWrapper
from cyborg.agents.Wrappers.IntListToAction import IntListToActionWrapper
from cyborg.agents.Wrappers.OpenAIGymWrapper import OpenAIGymWrapper

MAX_STEPS_PER_GAME = 20
MAX_EPS = 100

def run_training_example(scenario):
    print("Setup")
    path = str(inspect.getfile(Main))
    path = path[:-7] + f'/Shared/Scenarios/{scenario}.yaml'

    agent_name = 'Red'
    cyborg = OpenAIGymWrapper(agent_name=agent_name, env=IntListToActionWrapper(FixedFlatWrapper(Main(path, 'sim'))))

    observation = cyborg.reset(agent=agent_name)
    action_space = cyborg.get_action_space(agent_name)
    print(f"Observation size {len(observation)}, Action Size {action_space}")
    action_count = 0
    agent = TestAgent()
    for i in range(MAX_EPS):  # laying multiple games
        # print(f"\rTraining Game: {i}", end='', flush=True)
        reward = 0
        for j in range(MAX_STEPS_PER_GAME):  # step in 1 game
            action = agent.get_action(observation, action_space)
            next_observation, r, done, info = cyborg.step(action=action)
            action_space = info.get('action_space')
            reward += r

            agent.train(observation)  # training the agent
            observation = next_observation
            if done or j == MAX_STEPS_PER_GAME - 1:
                # print(f"Training reward: {reward}")
                break
        observation = cyborg.reset(agent=agent_name)
        agent.end_episode()

if __name__ == "__main__":
    run_training_example('Scenario1')
