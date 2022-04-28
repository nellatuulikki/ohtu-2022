import unittest
from player_reader import Player
from statistics import Statistics

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_with_valid_name(self):
        player = self.statistics.search("Semenko")
        self.assertEqual("Semenko", player.name)

    def test_search_with_invalid_name(self):
        self.assertEqual(self.statistics.search("Selänne"), None)

    def test_top_scorers(self):
        players = self.statistics.top_scorers(2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
    
    def test_team(self):
        players = self.statistics.team('EDM')
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")
    
    