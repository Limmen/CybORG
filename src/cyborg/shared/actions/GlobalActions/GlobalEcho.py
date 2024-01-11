# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Observation import Observation
from cyborg.shared.actions.GlobalActions.GlobalAction import GlobalAction


class GlobalEcho(GlobalAction):

    def __init__(self, echo_cmd):
        super().__init__()
        self.cmd = echo_cmd

    def emu_execute(self, team_server) -> Observation:
        raise ValueError("Not implemented")
