"""
This class defines a game with the logic for determining the winner of each round.
"""


class Game:
    def __init__(self, num_round, human):
        self.number_of_rounds = num_round
        self.human_player = human
        self.result_dict = {'r': {'r': 0, 'p': -1, 's': 1},
                            'p': {'r': 1, 'p': 0, 's': -1},
                            's': {'r': -1, 'p': 1, 's': 0}}
        self.human_wins = 0
        self.ai_wins = 0

    def round_result(self, player1_move, player2_move):
        result = self.result_dict[player1_move][player2_move]
        return result
