"""
Output général
"""
import itertools
from operator import itemgetter
from Models.Player import Player
from Models.Tournament import Tournament
from default_values import NB_PLAYERS

# JOUEUR
def created_player(player):
    print(f"{player.last_name} {player.first_name} créé(e) avec l'ID n°{player.id}")


def ranking_modified(player):
    print(f"Nouveau classement de {player.first_name} {player.last_name} : {player.ranking}")


def unique_id_returned(unique_id):
    print("\nL'ID du joueur concerné est le ", unique_id)


def sort_players_and_display(order):
    players_obj = Player.return_all_players()
    players_ser = []
    players_sorted = []

    for player in players_obj:
        players_ser.append(player.serialized_player())
    if order == 'alphabetical':
        print("\n-------- JOUEURS PRESENTS DANS LA BASE - Ordre Alphabétique --------")
        players_sorted = sorted(players_ser, key=itemgetter('Nom'), reverse=False)
    elif order == 'by ranking':
        print("\n-------- JOUEURS PRESENTS DANS LA BASE - Par Classement --------")
        players_sorted = sorted(players_ser, key=itemgetter('Classement'), reverse=True)

    for player in players_sorted:
        print(player_to_display(player))

    print("\n------------------------ Fin ------------------------\n")


def player_to_display(player):
    return f"\n- {player['Nom']} {player['Prenom']} - ID n°{player['ID']} - Classement actuel = {player['Classement']}"


def player_already_exist(player):
    print(f"Le joueur existe déjà dans la base de données sous le n°{player.id}- "
          "il sera rajouté dans le tournoi avec les informations déjà connues")


def player_not_exist():
    print("Le joueur recherché n'existe pas - Créez le ou ajoutez en un autre")


# TOURNOI

def tournament_created(tournament):
    print(f"\n-------- Tournoi n°{tournament.unique_id} --------\n")
    print(f"Tournoi de {tournament.name} qui se déroulera à {tournament.location}")
    if tournament.end:
        print(f"Date du tournoi : du {tournament.start} au {tournament.end}")
    elif not tournament.end:
        print(f"Date du tournoi : le {tournament.start}")
    print(f"Il sera composé de {tournament.rounds} rounds et de {NB_PLAYERS} joueurs.\n"
          f"Les règles de contrôle du temps seront celles du {tournament.time_control}\n")
    print("------------- Fin -------------\n")


def display_all_tournaments():
    tournaments = Tournament.return_all_tournaments()
    print("\n-------- Affichage des Tournois présents dans la base --------")
    for tournament in tournaments:
        tournament_created(tournament)
    print("\n------------------------ Fin ------------------------\n")


def no_tournament_find():
    print("\nAucun tournoi trouvé avec cet ID - Veuillez sélectionner un ID valide !")


def round_in_progress(round_to_play):
    print(f"\n----- DEBUT DU ROUND N°{round_to_play} ----- \n")


def display_match(list_of_matchs, round_to_play):
    print(f"\n-------------- ROUND {round_to_play} --------------\n")
    for match_number, match in enumerate(list_of_matchs):
        print(f"Match n°{match_number + 1} - {match[0]['Nom']} contre {match[1]['Nom']}")


def display_match_bis(matchs):
    for match in matchs.values():
        print(f"\n{match[0]['Nom']} {match[0]['Prenom']} contre "
              f"{match[1]['Nom']} {match[1]['Prenom']}")


def display_results_title():
    print("\n\n----- GENERATION DES RESULTATS DU ROUND ------\n\n"
          "match nul tapez 0\nvictoire joueur 1 tapez 1\nvictoire joueur 2 tapez 2\n\n")


def tournament_is_ending(players_of_tournament):
    print("\n\n----- LE TOURNOI EST TERMINE ! -----\n")
    players_of_tournament = sorted(players_of_tournament, key=itemgetter('Classement'), reverse=True)
    final_classification = sorted(players_of_tournament, key=itemgetter('Score'), reverse=True)
    print(f"Le vainqueur de ce tournoi est {final_classification[0]['Prenom']} {final_classification[0]['Nom']}\n")
    print(" --- Classement final ---\n")
    for place, player in enumerate(final_classification):
        print(f"{place + 1} - {player['Nom']} {player['Prenom']} ---- Score : {player['Score']}")
    print("")


def display_matchs_per_round(tournament):
    matchs = tournament.return_all_matchs()
    all_matchs = []
    for match in matchs:
        all_matchs.append(match)

    print("\n\n----- TOUS LES MATCHS DU TOURNOI - ROUND PAR ROUND -----\n")
    for round_number, rounds in enumerate(all_matchs):
        print(f"\n----- ROUND {round_number + 1} -----")
        for match_number, match in enumerate(rounds):
            print(f"Match n°{match_number + 1} - {match[0]['Nom']} contre {match[1]['Nom']}")
    print('\n----------   FIN   ----------')


def display_all_matchs_of_tournament(tournament):
    matchs = tournament.return_all_matchs()
    all_matchs = []
    for match in matchs:
        all_matchs.append(match)

    print("\n\n----- TOUS LES MATCHS DU TOURNOI -----\n")
    flat_list_of_matchs = itertools.chain(*all_matchs)
    for nb, match in enumerate(flat_list_of_matchs):
        print(f"Match n°{nb + 1} - {match[0]['Nom']} contre {match[1]['Nom']}")
    print('\n----------   FIN   ----------')
