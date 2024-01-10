# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Actions.ShellActionsFolder.ShellAction import ShellAction
from cyborg.simulator.State import State


class OpenConnection(ShellAction):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state: State):
        pass
