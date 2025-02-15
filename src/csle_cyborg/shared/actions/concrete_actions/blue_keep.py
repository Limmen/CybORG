from ipaddress import IPv4Address

from csle_cyborg.shared.observation import Observation
from csle_cyborg.shared.actions.concrete_actions.exploit_action import ExploitAction
from csle_cyborg.shared.enums import OperatingSystemPatch, OperatingSystemType, OperatingSystemDistribution
from csle_cyborg.simulator.host import Host
from csle_cyborg.simulator.process import Process
from csle_cyborg.simulator.state import State


class BlueKeep(ExploitAction):
    def __init__(self, session: int, agent: str, ip_address: IPv4Address, target_session: int):
        super().__init__(session, agent, ip_address, target_session)

    def sim_execute(self, state: State) -> Observation:
        return self.sim_exploit(state, 3389, 'rdp')

    def test_exploit_works(self, target_host: Host, vuln_proc: Process):
        # the exact patches and OS distributions are described here:
        # https://borncity.com/win/2019/06/06/how-to-bluekeep-check-for-windows/
        works = target_host.os_type == OperatingSystemType.WINDOWS and \
                ((OperatingSystemPatch.KB4500331 not in target_host.patches
                  and (target_host.distribution == OperatingSystemDistribution.WINDOWS_XP
                       or target_host.distribution == OperatingSystemDistribution.WINDOWS_SVR_2003SP2))
                 or (OperatingSystemPatch.KB4499149 not in target_host.patches
                     and OperatingSystemPatch.KB4499180 not in target_host.patches
                     and (target_host.distribution == OperatingSystemDistribution.WINDOWS_VISTA
                          or target_host.distribution == OperatingSystemDistribution.WINDOWS_SVR_2008SP1))
                 or (OperatingSystemPatch.KB4499164 not in target_host.patches
                     and OperatingSystemPatch.KB4499175 not in target_host.patches
                     and (target_host.distribution == OperatingSystemDistribution.WINDOWS_SVR_2008R2
                          or target_host.distribution == OperatingSystemDistribution.WINDOWS_7SP1)))

        works = True
        return works
