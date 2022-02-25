from Models.Player import Player
from Views.Input import name, date_of_birth, ranking, gender, return_player_with_unique_id
import random
import string


def create_new_player():

    unique_id = int(create_id_unique_for_player())
    first_name = name('first_name').upper()
    if first_name == '<-':
        return
    last_name = name('last_name').capitalize()
    if last_name == '<-':
        return
    user_date_of_birth = date_of_birth()
    user_gender = gender()
    user_ranking = ranking()

    return unique_id, first_name, last_name, user_date_of_birth, user_gender, user_ranking


def modify_player_ranking():

    player = return_player_with_unique_id()
    if not player:
        player = 0
        new_ranking = 0
        return player, new_ranking
    new_ranking = ranking()

    return player, new_ranking


def find_unique_id():

    first_name = name('first_name')
    if first_name == '0':
        return
    last_name = name('last_name')
    if last_name == '0':
        return
    unique_id = Player.return_unique_id(first_name, last_name)
    return unique_id


def create_id_unique_for_player():

    length = 5
    nb = string.digits
    unique_id = ''.join(random.choice(nb) for _i in range(length))
    players_in_db = Player.return_all_players()
    for player in players_in_db:
        if unique_id == player.id:
            return create_id_unique_for_player()

    return unique_id
