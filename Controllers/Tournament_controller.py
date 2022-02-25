from itertools import combinations
from Views.Input import basic_informations, add_date, tournament_time_control, name
from Views.Output import player_not_exist
import random
import string
from default_values import NB_ROUNDS
from Models.Player import Player


def create_new_tournament():

    unique_id = int(create_id_unique_for_tournament())
    tournament_name = basic_informations('name')
    location = basic_informations('location')
    start_date, end_date = add_date()
    rounds = NB_ROUNDS
    round_to_play = 1
    time_control = tournament_time_control({1, 2, 3})
    description = basic_informations('description')

    return unique_id, tournament_name, location, start_date, end_date, rounds, round_to_play, time_control, description


def add_player_manually():

    first_name = name('first_name')
    last_name = name('last_name')

    player = Player.does_player_exist_in_db(first_name, last_name)
    if player:
        serialized_player = Player.serialized_player(player)
        return serialized_player
    else:
        player_not_exist()
        return


def generate_all_matchs(list_of_players):

    all_combinations = create_all_combinations(list_of_players)
    real_match = []
    players_already_assigned = []
    nb_match = 0
    nb_rounds = 0
    while nb_rounds != 4:
        compteur_1 = 0
        while nb_match != 4:
            if compteur_1 == 500:
                break
            possible = random.choice(all_combinations)
            if possible[0] in players_already_assigned or possible[1] in players_already_assigned:
                compteur_1 += 1
                pass
            else:
                real_match.append(possible)
                players_already_assigned.append(possible[0])
                players_already_assigned.append(possible[1])
                all_combinations.remove(possible)
                nb_match += 1

        nb_rounds += 1
        nb_match = 0
        players_already_assigned = []

    nb_matchs_in_final_list = len(real_match)
    # On divise la liste en 4 pour les 4 tours
    row = 4
    col = 4
    real_match = [real_match[col * i: col * (i + 1)] for i in range(row)]

    return real_match, nb_matchs_in_final_list


def create_all_combinations(list_of_players):

    matchs = []
    combination_match = combinations(list_of_players, 2)
    for comb in combination_match:
        matchs.append(comb)

    return matchs


def create_id_unique_for_tournament():

    length = 4
    nb = string.digits
    unique_id = ''.join(random.choice(nb) for _i in range(length))

    return unique_id
