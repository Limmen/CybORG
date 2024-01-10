# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Actions.MSFActionsFolder.MSFAction import MSFAction
from cyborg.simulator.State import State


class MSFScanner(MSFAction):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state: State):
        pass
