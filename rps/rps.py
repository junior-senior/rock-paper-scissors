"""
This is the main script for the game. It defines the player input, and the main game loop.
"""

import player as p
import game as g

ai_player = p.AIPlayer()
num_rounds = 0
current_round = 0
move_set = ['Rock (r/R)', 'Paper (p/P)', 'Scissors (s/S)']

valid_player_move = False
player_move = ''


print('Welcome to Rock, Paper, Scissors.')

player_name = input('Please enter your name. ')
human = p.HumanPlayer(player_name)
game = g.Game(num_rounds, human)

print(f'Hello {player_name}.')
while num_rounds == 0:
    num_rounds = input('Please enter the number of rounds you would like to play. ')
    try:
        num_rounds = int(num_rounds)
    except ValueError:
        print('Please enter a valid integer.')
        num_rounds = 0

while current_round < num_rounds:
    print(f'The current score is: You {game.human_wins}:{game.ai_wins} Computer')
    while not valid_player_move:
        player_move = input(f'Please choose your move from: {move_set} ').lower()
        if player_move in human.move_set:
            valid_player_move = True
        else:
            print('Please enter a valid move. \'r\' or \'R\' for Rock, '
                  '\'p\' or \'P\' for Paper, \'s\' or \'S\' for Scissors. ')
    ai_move = ai_player.random_move()
    result = game.round_result(player_move, ai_move)
    if result == 1:
        print(f'{player_move} beats {ai_move}. You win this round.')
        current_round += 1
        game.human_wins += 1
    elif result == -1:
        print(f'{ai_move} beats {player_move}. The Computer wins this round.')
        current_round += 1
        game.ai_wins += 1
    elif result == 0:
        print('It is a draw! Play the round again')
    else:
        assert False
    valid_player_move = False
else:
    print(f'The final score is: You {game.human_wins}:{game.ai_wins} Computer')


