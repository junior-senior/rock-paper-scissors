import unittest
import game as g
import player


class TestGame(unittest.TestCase):

    human = player.HumanPlayer('Jake')
    game = g.Game(1, human)

    def test_human_player_wins(self, game):
        result = game.round_result('r', 'p')
        self.assertEqual(result, 1)

    def test_ai_player_wins(self, game):
        result = game.round_result('p', 's')
        self.assertEqual(result, -1)

    def test_both_moves_the_same(self, game):
        result = game.round_result('r', 'p')
        self.assertEqual(result, 0)
