# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Actions.Action import Action
from cyborg.shared.Observation import Observation


class ActionHandler:
    def __init__(self):
        pass

    def perform(self, action: Action) -> Observation:
        raise NotImplementedError
