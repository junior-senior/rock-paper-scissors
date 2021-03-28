import unittest
from data import load_data


class TestLoadData(unittest.TestCase):
    def test_load_data_player_not_found(self):
        player = 'Bob'
        bob_found, _ = load_data(player)
        self.assertFalse(bob_found)

    def test_load_data_player_found(self):
        player = 'test'
        test_found, _ = load_data(player)
        self.assertTrue(test_found)
