# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.msf_actions_folder.msf_action import MSFAction


class MSFPrivilegeEscalation(MSFAction):
    def __init__(self):
        super().__init__()

    def sim_execute(self, state):
        pass