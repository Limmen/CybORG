# Copyright DST Group. Licensed under the MIT license.
from CybORG.CybORG import ShellAction


class Persistence(ShellAction):
    def __init__(self, session, agent):
        super().__init__(session, agent)

    def sim_execute(self, state):
        pass