"""
This class defines a game with the logic for determining the winner of each round.
"""


class Game:
    def __init__(self, num_round, human):
        """
        :param num_round: The number of rounds the user has chosen to play.
        :param human: The user playing the game.
        """
        self.number_of_rounds = num_round
        self.human_player = human
        self.result_dict = {'r': {'r': 0, 'p': -1, 's': 1},
                            'p': {'r': 1, 'p': 0, 's': -1},
                            's': {'r': -1, 'p': 1, 's': 0}}
        self.human_wins = 0
        self.ai_wins = 0

    def round_result(self, player1_move, player2_move):
        """
        :param player1_move: The move chosen by the human player.
        :param player2_move: The move chosen by the AI player.
        :return: 1 for a user win, 0 for a tie and -1 for an AI win.
        """
        try:
            result = self.result_dict[player1_move][player2_move]
        except KeyError:
            print('Invalid Move')
        else:
            return result
