# Copyright DST Group. Licensed under the MIT license.
from cyborg.agents.SimpleAgents.BaseAgent import BaseAgent
from cyborg.shared.Actions.Action import Sleep


class SleepAgent(BaseAgent):
    def __init__(self):
        pass

    def train(self, results):
        pass

    def get_action(self, observation, action_space):
        return Sleep()

    def end_episode(self):
        pass

    def set_initial_values(self, action_space, observation):
        pass
