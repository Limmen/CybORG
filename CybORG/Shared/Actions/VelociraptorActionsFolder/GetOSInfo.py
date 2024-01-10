# Copyright DST Group. Licensed under the MIT license.

from CybORG.CybORG import QueryType
from CybORG.CybORG import Observation

from .VelociraptorAction import VelociraptorAction


class GetOSInfo(VelociraptorAction):

    def __init__(self, session: int, agent: str):
        super().__init__(session=session,
                         query_type=QueryType.ASYNC,
                        agent=agent)
        self.agent = agent

    def sim_execute(self, state):
        obs = Observation()
        return obs