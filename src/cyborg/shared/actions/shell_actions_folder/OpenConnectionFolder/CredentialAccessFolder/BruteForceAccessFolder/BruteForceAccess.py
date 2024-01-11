# Copyright DST Group. Licensed under the MIT license.n
from cyborg.shared.actions.shell_actions_folder.OpenConnectionFolder.CredentialAccessFolder.CredentialAccess import (
    CredentialAccess)


class BruteForceAccess(CredentialAccess):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state):
        pass
