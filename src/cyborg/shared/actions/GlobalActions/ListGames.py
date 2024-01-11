# Copyright DST Group. Licensed under the MIT license.
from cyborg.shared.Observation import Observation
from cyborg.shared.actions.GlobalActions.GlobalAction import GlobalAction


class ListGames(GlobalAction):
    """Get a list of all active games """

    def emu_execute(self, team_server) -> Observation:
        self._log_info("Listing games")
        obs = Observation()
        game_ids = team_server.get_games_list()
        obs.set_success(True)
        obs.add_key_value("game_ids", game_ids)
        return obs
