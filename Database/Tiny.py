
from tinydb import TinyDB


class Database:

    def __init__(self):
        self.db_tournament = TinyDB('tournament.json')
        self.tournament_table = self.db_tournament.table('Tournaments')
        self.db_players = TinyDB('players.json')
        self.players_table = self.db_players.table('Players')

    def insert_players(self, serialized_players):
        self.players_table.insert_multiple(serialized_players)

    def return_players(self):
        serialized_players = self.players_table.all()
        return serialized_players

    def insert_tournament(self, serialized_tournament):
        self.tournament_table.insert_multiple(serialized_tournament)

    def return_tournaments(self):
        serial_tournaments = self.tournament_table.all()
        return serial_tournaments

    def delete_tables(self):
        self.players_table.truncate()
        self.tournament_table.truncate()
