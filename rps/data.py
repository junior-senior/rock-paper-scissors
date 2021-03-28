
def load_data(player):
    saved_data = None
    player_found = False
    player_data = None
    with open('../saved_data.txt') as f:
        saved_data = f.readlines()[1:]
        for data in saved_data:
            if player in data.split(',')[0]:
                player_found = True
                player_data = data.split(',')[1:]
                if player_data:
                    player_data_dict = {data.split(':')[0].strip(): data.split(':')[1].strip()
                                        for data in player_data}
            return player_found, player_data_dict

