# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.msf_actions_folder.MSFAction import MSFAction


class RemoteCodeExecution(MSFAction):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state):
        pass
