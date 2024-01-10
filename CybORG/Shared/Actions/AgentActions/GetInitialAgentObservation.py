# Copyright DST Group. Licensed under the MIT license.
from CybORG.CybORG import Observation

from .AgentAction import AgentAction


class GetInitialAgentObservation(AgentAction):
    """Get the initial observation for an agent. """

    def emu_execute(self, agent, *args, **kwargs) -> Observation:
        return agent.init_observation
