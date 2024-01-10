# These tests check that the green actions are working:
# DiscoverRemoteSystems, DiscoverNetworkServices, ExploitService, Escalate, Impact

# tests need to check that a range of inputs result in the correct changes to the state and return the correct obs
# tests should establish varying environmental states that results in these actions performing differently
from ipaddress import IPv4Network, IPv4Address

from CybORG.CybORG import CybORG
import inspect

from CybORG.CybORG import GreenAgent

from CybORG.CybORG import TrinaryEnum, ProcessType, ProcessState, SessionType
from CybORG.CybORG import Win2008EphemeralPort
import pytest

def test_GreenAgent():
    # Create cyborg environment
    path = str(inspect.getfile(CybORG))
    path = path[:-10] + '/Shared/Scenarios/Scenario1b.yaml'
    cyborg = CybORG(path, 'sim',agents={'Green': GreenAgent})

    # Setup Agent
    action_space = cyborg.get_action_space('Green')
    session = action_space['session']
    assert session

