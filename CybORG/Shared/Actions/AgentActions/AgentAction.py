# Copyright DST Group. Licensed under the MIT license.
from CybORG.CybORG import Observation
from CybORG.CybORG import Action


class AgentAction(Action):
    """Abstract class for an agent level action.

    An agent action is one that operates within the context of a single
    scenario/game instance, within an single agent, but outside of a
    single session.

    Examples would be:
    - creating a new session
    - terminating a session
    - listing available sessions in a game
    """

    def emu_execute(self, agent, *args, **kwargs) -> Observation:
        raise NotImplementedError
