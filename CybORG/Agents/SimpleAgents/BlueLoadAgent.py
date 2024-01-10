import inspect

from stable_baselines3 import PPO

from CybORG.CybORG import CybORG
from CybORG.CybORG import BaseAgent
from CybORG.CybORG import EnumActionWrapper
from CybORG.CybORG import FixedFlatWrapper
from CybORG.CybORG import OpenAIGymWrapper
from CybORG.CybORG import ReduceActionSpaceWrapper
from CybORG.CybORG import ChallengeWrapper

class BlueLoadAgent(BaseAgent):
    # agent that loads a StableBaselines3 PPO model file
    def train(self, results):
        pass

    def end_episode(self):
        pass

    def set_initial_values(self, action_space, observation):
        pass

    def __init__(self, model_file: str = None):
        if model_file is not None:
            self.model = PPO.load(model_file)
        else:
            self.model = None

    def get_action(self, observation, action_space):
        """gets an action from the agent that should be performed based on the agent's internal state and provided observation and action space"""
        if self.model is None:
            path = str(inspect.getfile(CybORG))
            path = path[:-10] + '/Shared/Scenarios/Scenario1b.yaml'
            cyborg = ChallengeWrapper(env=CybORG(path, 'sim'), agent_name='Blue')
            self.model = PPO('MlpPolicy', cyborg)
        action, _states = self.model.predict(observation)
        return action