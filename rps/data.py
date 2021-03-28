def load_data(player):
    """
    This function is called after the user has entered their name to determine whether they have a high score saved.
    :param player: The name of the human who was playing the game.
    :return: player_found bool, player_data, which is the highest score the player has achieved.
    """
    saved_data = None
    player_found = False
    player_data = None
    with open('../saved_data.txt') as f:
        saved_data = f.readlines()[1:]
        for data in saved_data:
            if player in data.split(',')[0]:
                player_found = True
                player_data = data.split(', ')[1]
            return player_found, player_data


def save_data(player, player_data):
    """
    This function is called once the number of rounds have been played.
    :param player: The name of the human who was playing the game.
    :param player_data: The score of the match.
    :return: Nothing
    """
    player_found = False
    saved_data = None
    new_data = []
    match_score = int(player_data.split('-')[0])
    with open('../saved_data.txt') as f:
        saved_data = f.readlines()
        for i, data in enumerate(saved_data):
            if player in data.split(',')[0] and i > 0: # If the player is on that line and it is not the first line.
                player_found = True
                highest_human_score = int(data.split(', ')[1].split('-')[0])
                if match_score > highest_human_score: # If the player's last highest score is greater than the last
                    new_data.append(player + ', ' + player_data + '\n')
                else:  # If it wasn't use the old data
                    new_data.append(data)
            else:  # If the player wasn't found or it's the header line
                new_data.append(data)
        else:
            if not player_found:  # If the player wasn't found (New player)
                new_data.append(player + ', ' + player_data + '\n')

    # Write updated data to file
    with open('../saved_data.txt', 'w') as f:
        for line in new_data:
            f.writelines(line)
