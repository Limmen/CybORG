# Copyright DST Group. Licensed under the MIT license.
from CybORG.CybORG import InternalEnumeration


class HostInfoEnumeration(InternalEnumeration):

    def __init__(self, session: int, agent: str = None):
        super().__init__(session, agent)

    def sim_execute(self, state):
        pass
