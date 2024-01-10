# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.msf_actions_folder.meterpreter_actions_folder.meterpreter_action import MeterpreterAction
from cyborg.shared.enums import SessionType
from cyborg.shared.observation import Observation
from cyborg.simulator.state import State


# Call reboot from a meterpreter session - reboots dict that session is on
# This deletes all non-default processes, and deletes all files in the /tmp/ folder
class MeterpreterReboot(MeterpreterAction):
    def __init__(self, session: int, agent: str, target_session: int):
        super().__init__(session=session, agent=agent, target_session=target_session)

    def sim_execute(self, state: State):
        obs = Observation()
        obs.set_success(False)
        if self.session not in state.sessions[self.agent]:
            return obs


        if self.session not in state.sessions[self.agent] or state.sessions[self.agent][
            self.session].session_type != SessionType.MSF_SERVER:
            return obs
        if self.meterpreter_session not in state.sessions[self.agent] or state.sessions[self.agent][
            self.meterpreter_session].session_type != SessionType.METERPRETER:
            return obs
        if state.sessions[self.agent][self.session].active and state.sessions[self.agent][self.meterpreter_session].active:
            host = state.sessions[self.agent][self.meterpreter_session].host
            obs.set_success(True)
            state.reboot_host(host)

        return obs