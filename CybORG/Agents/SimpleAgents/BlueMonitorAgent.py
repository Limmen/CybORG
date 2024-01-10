from CybORG.Shared.Actions.AbstractActions.Monitor import Monitor
from CybORG.Agents.SimpleAgents.BaseAgent import BaseAgent

class BlueMonitorAgent(BaseAgent):
    def __init__(self):
        pass

    def get_action(self,observation,action_space):
        session = 0
        return Monitor(session=session,agent='Blue')


    def train(self, results):
        pass

    def end_episode(self):
        pass

    def set_initial_values(self, action_space, observation):
        pass
