from ipaddress import IPv4Address

from cyborg.shared.Observation import Observation
from cyborg.shared.Actions.ConcreteActions.ExploitAction import ExploitAction
from cyborg.shared.Enums import OperatingSystemPatch, OperatingSystemType
from cyborg.simulator.Host import Host
from cyborg.simulator.Process import Process
from cyborg.simulator.State import State


class EternalBlue(ExploitAction):
    def __init__(self, session: int, agent: str, ip_address: IPv4Address, target_session: int):
        super().__init__(session, agent, ip_address, target_session)

    def sim_execute(self, state: State) -> Observation:
        return self.sim_exploit(state, 139, 'smb')

    def test_exploit_works(self, target_host: Host, vuln_proc: Process):
        # check if OS and process information is correct for exploit to work
        return target_host.os_type == OperatingSystemType.WINDOWS and OperatingSystemPatch.MS17_010 not in target_host.patches
