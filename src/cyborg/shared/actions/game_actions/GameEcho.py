# Copyright DST Group. Licensed under the MIT license.

from cyborg.shared.actions.game_actions.GameAction import GameAction


class GameEcho(GameAction):

    def __init__(self, echo_cmd: str):
        super().__init__()
        self.cmd = echo_cmd
