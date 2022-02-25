"""
Affichage du menu
"""

from Views.Input import user_choice_menu


def program_title():
    print("\n======== GESTIONNAIRE DE TOURNOIS D'ECHECS ===========\n")


def display_main_menu():
    print("\n-----  Menu Principal  -----\n")
    print("1. Création et Modification de Joueur\n"
          "2. Création de Tournoi\n"
          "3. Démarrer ou Continuer un Tournoi\n"
          "4. Interface Rapports\n\n"
          "9. Quitter le programme\n")

    choice = user_choice_menu({1, 2, 3, 4, 9})
    return choice


def display_player_menu():
    print("\n-----  Création et Modification de Joueur  -----\n")
    print("1. Créer un nouveau Joueur\n"
          "2. Modifier le classement d'un joueur\n"
          "3. Retrouver l'ID d'un joueur\n\n"
          "9. Retour au menu principal\n")

    choice = user_choice_menu({1, 2, 3, 9})
    print("")
    return choice


def add_players_in_tournament_menu():
    print("\n-----  Ajout des joueurs  -----\n")
    print("1. Import Manuel\n\n"
          "2. [VERSION DEMO] Import automatique des joueurs\n")

    choice = user_choice_menu({1, 2})
    return choice


def manual_import():
    print("\n\n1. Création d'un nouveau joueur\n"
          "\n2. Import d'un joueur depuis la base de données\n")

    choice = user_choice_menu({1, 2})
    return choice


def display_report_menu():
    print("\n-----  Interface Rapports  -----\n")
    print("Rapports Joueurs :\n"
          "1. Afficher tous les joueurs de la base - Par ordre alphabétique\n"
          "2. Afficher tous les joueurs de la base - Par Classement\n\n"
          "Rapports Tournoi :\n"
          "3. Afficher tous les tournois de la base\n"
          "4. Afficher tous les rounds d'un tournoi\n"
          "5. Afficher tous les matchs d'un tournoi\n\n"
          "9. Retour au menu principal\n")

    choice = user_choice_menu({1, 2, 3, 4, 5, 9})
    return choice
