"""
Input général
"""

import datetime
from default_values import TIME_CONTROL
from Models.Player import Player


# MENU
def user_choice_menu(possibilities):
    try:
        choice = int(input("\nVeuillez indiquer votre choix : "))
        if choice not in possibilities:
            print("\nMauvais choix ! Veuillez renseigner un choix valide")
            return user_choice_menu(possibilities)
        else:
            return choice
    except ValueError:
        print("\nValeur incorrecte - Veuillez saisir un chiffre svp !")
        return user_choice_menu(possibilities)

# INPUT JOUEUR
def date_of_birth():
    user_date_of_birth = input("Date de naissance (JJ/MM/AAAA) : ")
    try:
        datetime.datetime.strptime(user_date_of_birth, "%d/%m/%Y")
        return user_date_of_birth
    except ValueError:
        print("Cette date n'est pas valide - Merci d'en saisir une nouvelle")
        return date_of_birth()


def gender():
    try:
        user_gender = str(input("Sexe du joueur (M ou F) : "))
        if user_gender in {"M", "F"}:
            return user_gender
        else:
            print("Veuillez saisir une informations valide !")
            return gender()
    except ValueError:
        print("Veuillez saisir une informations valide !")
        return gender()


def ranking():
    try:
        user_ranking = int(input("Classement du joueur (Positif obligatoirement) : "))
        if user_ranking < 0:
            print("Le classement est obligatoirement positif - Réessayez !")
            return ranking()
        else:
            print("")
            return user_ranking
    except ValueError:
        print("Mauvaise saisie - Réessayez !")
        return ranking()


def name(type_of_name):
    if type_of_name == 'first_name':
        return input("Nom de famille : ")
    elif type_of_name == 'last_name':
        return input('Prénom : ')


# INPUT POUR TROUVER UN JOUEUR AVEC SON ID
def return_player_with_unique_id():
    try:
        unique_id = int(input("Indiquez l'ID du joueur : "))
        if unique_id == 0:
            return
        player = Player.return_player(unique_id)
        if not player:
            print("Ce joueur n'existe pas dans la base de données - Réessayez svp !")
            return return_player_with_unique_id()
        else:
            return player
    except ValueError:
        print("Veuillez renseigner une information valide svp !")
        return return_player_with_unique_id()

# INPUT TOURNOI
def basic_informations(type_of_information):
    information = ''
    if type_of_information == 'name':
        information = input("\nNom du tournoi : ")
    elif type_of_information == 'location':
        information = input("Lieu du tournoi : ")
    elif type_of_information == 'description':
        information = input("Description du tournoi : ")

    return information

def add_date():
    """
    if ( date début == date de fin ) :
        return date début
    else :
        return les 2 dates : "du JJ/MM/AAAA au JJ/MM/AAAA"
    """
    try:
        duration = input("Tournoi sur plusieurs jours ? (O/N) ")
        if duration == "O":
            start_date, formatted_start_date = start_and_end_date('start')
            end_date, formatted_end_date = start_and_end_date('end')
            if formatted_start_date > formatted_end_date:
                print("La date de début du tournoi ne peut être "
                      "après la date de fin du tournoi - Merci de recommencer")
                return add_date()
            return start_date, end_date
        elif duration == "N":
            start_date, formatted_start_date = start_and_end_date('day_only')
            end_date = None
            return start_date, end_date
        elif duration not in {"O", "N"}:
            print("Veuillez saisir O ou N svp !")
            return add_date()
    except ValueError:
        print("Veuillez saisir une valeur valide !")
        return add_date()


def start_and_end_date(moment):
    """
    Vérifie que les dates existentent
    """
    date = ""
    if moment == 'start':
        date = input("Début du tournoi : ")
    elif moment == 'end':
        date = input("Fin du tournoi : ")
    elif moment == 'day_only':
        date = input("Date du tournoi : ")
    try:
        formatted_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        return date, formatted_date
    except ValueError:
        print("Cette date n'est pas valide - Merci d'en saisir une nouvelle")
        return start_and_end_date(moment)


def tournament_time_control(possibilities):
    try:
        type_tc = int(input(f"Type de contrôle du temps (1. {TIME_CONTROL[0]} - 2. {TIME_CONTROL[1]} "
                            f"- 3. {TIME_CONTROL[2]}) : "))
        if type_tc not in possibilities:
            print("Veuillez choisir un choix entre 1 et 3 svp !")
            return tournament_time_control(possibilities)
        elif type_tc == 1:
            return TIME_CONTROL[0]
        elif type_tc == 2:
            return TIME_CONTROL[1]
        elif type_tc == 3:
            return TIME_CONTROL[2]
    except ValueError:
        print("Caractère non-valide - Merci de saisir un chiffre entre 1 et 3")
        return tournament_time_control(possibilities)


def return_tournament_id():
    try:
        unique_id = int(input("\nID du tournoi concerné : "))
        return unique_id
    except ValueError:
        print("Veuillez saisir un nombre positif svp")


def display_results(list_of_matchs, tournament):
    """
    L'user rentre les résultats du tour, les classement sont mis à jour
    si un joueur gagne un match, on ajoute +1 à player.score
    """
    for match_number, match in enumerate(list_of_matchs):
        print(f"Match n°{match_number + 1} - {match[0]['Nom']} contre {match[1]['Nom']}")
        try:
            result = int(input("Résultat du match : "))
            if result not in {0, 1, 2}:
                print("Veuillez indiquer 0, 1 ou 2 svp !")
                return display_results(list_of_matchs, tournament)
            else:
                if result == 1:
                    player = tournament.return_player(match[0]['ID'])
                    player['Score'] += 1
                elif result == 2:
                    player = tournament.return_player(match[1]['ID'])
                    player['Score'] += 1
                elif result == 0:
                    player = tournament.return_player(match[0]['ID'])
                    player['Score'] += 0.5
                    player = tournament.return_player(match[1]['ID'])
                    player['Score'] += 0.5
        except ValueError:
            print("Veuillez saisir un chiffre !")
            return display_results(list_of_matchs, tournament)


def continue_tournament():
    try:
        choice = input("\nContinuer le tournoi (O/N) : ").capitalize()
        if choice not in {'O', 'N'}:
            print("Merci de saisir O ou N")
            return continue_tournament()
        else:
            return choice
    except ValueError:
        print("Merci de saisir une information valide")
        return continue_tournament()
