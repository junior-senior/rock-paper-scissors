"""
This class defines the main Player class. An initial Player is defined and then a User and AI players will inherit
from that class.
"""

import random


class Player:
    """The Player class is used to define the base attributes used for the Human and AI players"""
    def __init__(self):
        self.current_score = 0
        self.move_set = ['r', 'p', 's']


class HumanPlayer(Player):
    """The human player only current has the name attribute. This will be expanded upon as the program is developed
        Args:
            :param Name (str): This is the player's name
    """
    def __init__(self, name):
        super().__init__()
        self.name = name


class AIPlayer(Player):
    def random_move(self):
        """Random move is only defined for the AI Player as the human player chooses their moves.
            :return move: The move selected at random by the AI using the random library.
        """
        move = random.choice(list(self.move_set))
        return move
