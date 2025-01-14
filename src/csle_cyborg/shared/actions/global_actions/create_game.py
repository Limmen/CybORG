# Copyright DST Group. Licensed under the MIT license.
from csle_cyborg.shared.observation import Observation
from csle_cyborg.shared.scenario import Scenario
from .global_action import GlobalAction


class CreateGame(GlobalAction):
    """Creates a new game """

    def __init__(self, scenario: Scenario):
        super().__init__()
        self.scenario = scenario

    def emu_execute(self, team_server, *args, **kwargs) -> Observation:
        self._log_info("Creating new game")
        obs = Observation()
        new_game = team_server.create_new_game(self.scenario, self.config)
        obs.set_success(True)
        obs.add_key_value("game_id", new_game.game_id)

        obs.add_key_value("ip_hostname_map", {v: k for k, v in new_game.network.ip_hostname_map.items()})
        obs.add_key_value("cidr_subnet_map", {v.name: v.cidr for k, v in new_game.network.cidr_subnet_map.items()})

        return obs
