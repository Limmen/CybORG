# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Actions.MSFActionsFolder.MeterpreterActionsFolder.MeterpreterAction import MeterpreterAction
from cyborg.simulator.Session import SessionType
from cyborg.shared.Observation import Observation
from cyborg.simulator.State import State


# Call localtime from a meterpreter session - gives the current local time of the dict
class LocalTime(MeterpreterAction):
    def __init__(self, session: int, agent: str):
        super().__init__(session=session, agent=agent)

    def sim_execute(self, state: State):
        obs = Observation()
        obs.set_success(False)
        if self.session not in state.sessions[self.agent]:
            return obs
        session = state.sessions[self.agent][self.session]

        if session.session_type != SessionType.METERPRETER or not session.active:
            return obs

        obs.set_success(True)
        obs.add_system_info(local_time=session.host.time)
        return obs
