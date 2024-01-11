# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.shell_actions_folder.ShellAction import ShellAction
from cyborg.simulator.State import State


class OpenConnection(ShellAction):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state: State):
        pass
