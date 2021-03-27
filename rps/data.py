"""
This script is responsible for validating user login
"""

class Data:
    def __init__(self):
        self.data_file = 'saved_data.txt'

    def load_player_data(self, player):
        with open(self.data_file) as f:
