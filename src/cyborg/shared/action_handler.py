# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.actions.action import Action
from cyborg.shared.observation import Observation


class ActionHandler:
    def __init__(self):
        pass

    def perform(self, action: Action) -> Observation:
        raise NotImplementedError
