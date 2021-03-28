"""
This class defines the main Player class. An initial Player is defined and then a User and AI players will inherit
from that class.
"""

import random


class Player:
    def __init__(self):
        self.name = ''
        self.current_score = 0
        self.move_set = ['r', 'p', 's']


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.password = ''


class AIPlayer(Player):
    def random_move(self):
        move = random.choice(list(self.move_set))
        return move
