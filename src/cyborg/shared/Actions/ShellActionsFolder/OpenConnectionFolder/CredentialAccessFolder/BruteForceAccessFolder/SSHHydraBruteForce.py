# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Actions.ShellActionsFolder.OpenConnectionFolder.CredentialAccessFolder.BruteForceAccessFolder.BruteForceAccess import BruteForceAccess


class SSHHydraBruteForce(BruteForceAccess):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state):
        pass