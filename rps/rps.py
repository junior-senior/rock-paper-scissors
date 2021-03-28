"""
This is the main script for the game. It defines the player input, and the main game loop.
"""

import player as p
import game as g
import data as d

ai_player = p.AIPlayer()
num_rounds = 0
current_round = 0
move_set_dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

valid_player_move = False
player_move = ''


print('Welcome to Rock, Paper, Scissors.')

player_name = input('Please enter your name. ')
human = p.HumanPlayer(player_name)
saved_data = None


print(f'Hello {player_name}.')
player_has_saved_data, player_data = d.load_data(player_name)

# While loop to make sure user enters a valid number
while num_rounds == 0:
    num_rounds = input('Please enter the number of rounds you would like to play. ')
    try:
        num_rounds = int(num_rounds)
    except ValueError:
        print('Please enter a valid integer.')
        num_rounds = 0

game = g.Game(num_rounds, human)

if player_data[str(num_rounds)]:
    print(f'The current high score for {num_rounds} rounds is {player_data[str(num_rounds)]}')

# Main game loop
while current_round < num_rounds:
    print(f'The current score is: You {game.human_wins}:{game.ai_wins} Computer')
    # While loop to make sure user enters an valid move
    while not valid_player_move:
        player_move = input(f'Please choose your move from: {move_set_dict} ').lower()
        if len(player_move) > 1:
            player_move = player_move[0]
        if player_move in human.move_set:
            valid_player_move = True
        else:
            print('Please enter a valid move. \'r\' or \'R\' for Rock, '
                  '\'p\' or \'P\' for Paper, \'s\' or \'S\' for Scissors. ')
    ai_move = ai_player.random_move()
    result = game.round_result(player_move, ai_move)

    if result == 1:
        print(f'{move_set_dict[player_move]} beats {move_set_dict[ai_move].lower()}. You win this round.\n')
        current_round += 1
        game.human_wins += 1
    elif result == -1:
        print(f'{move_set_dict[ai_move]} beats {move_set_dict[player_move].lower()}. The Computer wins this round.\n')
        current_round += 1
        game.ai_wins += 1
    elif result == 0:
        print('It is a draw! Play the round again.\n')
    else:
        assert False
    valid_player_move = False
else:
    print(f'The final score is: You {game.human_wins}:{game.ai_wins} Computer')


