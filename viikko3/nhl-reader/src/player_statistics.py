from unittest.case import _AssertRaisesContext

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def get_stats(self):
        return self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda x: x.nationality == nationality, self.get_stats())
        sorted_players = sorted(players, key=lambda x: x.get_all_points(), reverse=True)

        return sorted_players

