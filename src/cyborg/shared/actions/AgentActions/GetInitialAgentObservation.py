# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Observation import Observation
from cyborg.shared.actions.AgentActions.AgentAction import AgentAction


class GetInitialAgentObservation(AgentAction):
    """Get the initial observation for an agent. """

    def emu_execute(self, agent, *args, **kwargs) -> Observation:
        return agent.init_observation
