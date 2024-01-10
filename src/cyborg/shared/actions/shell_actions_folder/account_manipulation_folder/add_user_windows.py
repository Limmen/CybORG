# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.shell_actions_folder.account_manipulation_folder.account_manipulation import AccountManipulation
from cyborg.shared.enums import OperatingSystemType
from cyborg.shared.observation import Observation


class AddUserWindows(AccountManipulation):
    def __init__(self, session, agent, username, password):
        super().__init__(session, agent)
        self.username = username
        self.password = password

    def sim_execute(self, state):
        obs = Observation()
        obs.set_success(False)
        if self.session not in state.sessions[self.agent]:
            return obs

        if state.sessions[self.agent][self.session].active:
            host = state.sessions[self.agent][self.session].host
            obs.add_system_info(hostid="hostid0", os_type=host.os_type)
            if host.os_type == OperatingSystemType.WINDOWS:
                user = host.add_user(username=self.username, password=self.password)
                if user is not None:
                    obs.set_success(True)

                else:
                    obs.set_success(False)

            else:
                obs.set_success(False)
        else:
            obs.set_success(False)
        return obs