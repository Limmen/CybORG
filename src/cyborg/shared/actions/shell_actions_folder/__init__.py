from .internal_enumeration_folder import IFConfig, IPConfig, SystemInfo, Uname
from .credential_harvesting_folder import ReadShadowFile, ReadPasswdFile
from .network_scan_folder import NmapScan, PingSweep
from .open_connection_folder import \
    NetcatConnect, SSHAccess, SSHHydraBruteForce, SMBAnonymousConnection
from .DeleteFileWindows import DeleteFileWindows
from .KillProcessLinux import KillProcessLinux
from .persistence_folder import Schtasks
from .account_manipulation_folder import \
    AddUserWindows, DisableUserWindows, RemoveUserFromGroupWindows, \
    AddUserLinux, DisableUserLinux, RemoveUserFromGroupLinux
from .service_manipulation_folder import ShellStopService, StartService
from .shell_privilege_escalation_folder import \
    LinuxKernelPrivilegeEscalation, DirtyCowPrivilegeEscalation
from .ShellSleep import ShellSleep
from .FindFlag import FindFlag
from .DeleteFileWindows import DeleteFileWindows
from .DeleteFileLinux import DeleteFileLinux
from .KillProcessWindows import KillProcessWindows
from .ShellPS import ShellPS
from .ShellEcho import ShellEcho
