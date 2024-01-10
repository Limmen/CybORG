# Copyright DST Group. Licensed under the MIT license.
from CybORG.CybORG import Action
from CybORG.CybORG import Observation


class ActionHandler:
    def __init__(self):
        pass

    def perform(self, action: Action) -> Observation:
        raise NotImplementedError
