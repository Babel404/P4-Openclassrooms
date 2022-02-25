from Controllers.Player_controller import create_new_player, modify_player_ranking, find_unique_id
from Controllers.Match_controller import get_tournament_with_id, run_round
from Controllers.Tournament_controller import create_new_tournament, add_player_manually, generate_all_matchs
from Views.Menu import display_main_menu, display_player_menu, add_players_in_tournament_menu, manual_import, \
    display_report_menu
from Views.Output import created_player, ranking_modified, unique_id_returned, sort_players_and_display, \
    tournament_created, display_all_tournaments, player_already_exist, display_matchs_per_round, \
    display_all_matchs_of_tournament
from Models.Player import Player
from Models.Tournament import Tournament
from Database.Tiny import Database
from default_values import PLAYERS_DEMO, NB_PLAYERS


class MainController:

    def __init__(self):
        self.database = Database()

    def load_database(self):

        players = self.database.return_players()
        tournaments = self.database.return_tournaments()
        for player in players:
            Player(
                player['ID'],
                player['Nom'],
                player['Prenom'],
                player['Date_de_naissance'],
                player['Sexe'],
                player['Classement'],
                player['Score']
            )
        for tournament in tournaments:
            Tournament(
                tournament['ID'],
                tournament['Nom'],
                tournament['Lieu'],
                tournament['Date_de_debut'],
                tournament['Date_de_fin'],
                tournament['Nombre_de_rounds'],
                tournament['Time_control'],
                tournament['Description'],
                tournament['Round_a_jouer'],
                tournament['Joueurs'],
                tournament['Matchs']
            )
        self.main_menu()

    def main_menu(self):

        choice = display_main_menu()

        if choice == 1:  # Player interface
            self.player_menu()
        elif choice == 2:  # Tournament interface
            self.new_tournament()
        elif choice == 3:  # Begin or Continue a tournament
            self.begin_or_continue_tournament()
        elif choice == 4:  # Report interface
            self.report_menu()
            self.main_menu()
        elif choice == 9:  # Save and quit
            self.save_in_database()
            SystemExit(0)

    def save_in_database(self):

        self.database.delete_tables()
        serialized_players = Player.return_all_serialized_players()
        self.database.insert_players(serialized_players)
        serialized_tournaments = Tournament.return_all_serialized_tournament()
        self.database.insert_tournament(serialized_tournaments)

    def player_menu(self):

        choice = display_player_menu()

        if choice == 1:
            unique_id, first_name, last_name, date_of_birth, gender, ranking = \
                create_new_player()
            player_created = Player(unique_id, first_name, last_name, date_of_birth, gender, ranking, score=0)
            created_player(player_created)
            return self.player_menu()
        elif choice == 2:
            player, new_ranking = modify_player_ranking()
            if player == 0:
                return self.player_menu()
            else:
                print(player)
                player.modify_ranking(new_ranking)
                ranking_modified(player)
                return self.player_menu()
        elif choice == 3:
            unique_id = find_unique_id()
            if not unique_id:
                return self.player_menu()
            else:
                unique_id_returned(unique_id)
                return self.player_menu()
        elif choice == 9:
            return self.main_menu()

    def new_tournament(self):

        unique_id, tournament_name, tournament_location, \
            start_date, end_date, rounds, round_nb, time_control, tournament_description = create_new_tournament()

        choice = add_players_in_tournament_menu()
        players_for_tournament = []
        nb_players = NB_PLAYERS
        if choice == 1:  # Manual import
            while nb_players != 0:
                second_choice = manual_import()
                if second_choice == 1:  # Create a new player for the tournament
                    unique_id, first_name, last_name, date_of_birth, gender, ranking = \
                        create_new_player()
                    player_exist = Player.does_player_exist_in_db(first_name, last_name)
                    if player_exist:
                        player_already_exist(player_exist)
                        players_for_tournament.append(player_exist)
                    else:
                        player = Player(unique_id, first_name, last_name, date_of_birth,
                                        gender, ranking, score=0).serialized_player()
                        players_for_tournament.append(player)
                    nb_players -= 1
                elif second_choice == 2:  # Import a player form DB
                    player = add_player_manually()
                    if not player:
                        pass
                    else:
                        players_for_tournament.append(player)
                        nb_players -= 1
        elif choice == 2:  # Automatic import of players from default_values  -  DEMO VERSION
            players_for_tournament = PLAYERS_DEMO
            for player in players_for_tournament:
                player_exist = Player.does_player_exist_in_db(player['Nom'], player['Prenom'])
                if player_exist:
                    pass
                else:
                    Player(player['ID'], player['Nom'], player['Prenom'], player['Date_de_naissance'],
                           player['Sexe'], player['Classement'], player['Score'])

        tournament = Tournament(unique_id, tournament_name, tournament_location, start_date, end_date, rounds,
                                time_control, tournament_description, round_nb, players_for_tournament, matchs=None)

        all_matchs = generate_all_matchs(tournament.players)
        nb_matchs = 0
        while nb_matchs != 16:
            all_matchs, nb_matchs = generate_all_matchs(players_for_tournament)

        tournament.save_matchs(all_matchs)

        tournament_created(tournament)
        return self.main_menu()

    def begin_or_continue_tournament(self):

        tournament = get_tournament_with_id()
        if not tournament:
            return self.main_menu()

        run_round(tournament)

        return self.main_menu()

    def report_menu(self):

        choice = display_report_menu()

        if choice == 1:  # Display players in DB in alphabetical order
            sort_players_and_display('alphabetical')
            self.report_menu()
        elif choice == 2:  # Display players in DB by ranking
            sort_players_and_display('by ranking')
            self.report_menu()
        elif choice == 3:  # Display all the tournaments in DB
            display_all_tournaments()
            self.report_menu()
        elif choice == 4:  # Display all the matches of a tournament per rounds
            tournament = get_tournament_with_id()
            if not tournament:
                return self.main_menu()

            display_matchs_per_round(tournament)
            self.report_menu()
        elif choice == 5:  # Display all the matches of a tournament
            tournament = get_tournament_with_id()
            if not tournament:
                return self.main_menu()

            display_all_matchs_of_tournament(tournament)
            self.report_menu()
        elif choice == 9:  # Back to main menu
            return
