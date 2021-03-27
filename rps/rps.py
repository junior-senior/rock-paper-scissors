"""
This is the main script for the game. It defines the player input, and the main game loop.
"""

import player as p
import game as g


print('Welcome to Rock, Paper, Scissors.')
player_name = input('Please enter your name. ')
human = player_name
ai_player = p.AIPlayer()
num_rounds = 0
while num_rounds == 0:
    num_rounds = input('Please enter the number of rounds you would like to play. ')
    try:
        num_rounds = int(num_rounds)
    except ValueError:
        print('Please enter a valid integer.')
current_round = 0

game = g.Game(num_rounds, human)
move_set = ['Rock (r)', 'Paper (p)', 'Scissors (s)']

while current_round < num_rounds:
    player_move = input('Please choose your move from: '.join(move_set))
    ai_move = ai_player.random_move()