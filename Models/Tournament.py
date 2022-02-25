
class Tournament:
    TOURNAMENTS = []
    SERIALIZED_TOURNAMENTS = []

    def __init__(self, unique_id, tournament_name, tournament_location,
                 start_date, end_date, rounds, tournament_time_control, tournament_description,
                 round_to_play, players, matchs):
        self.unique_id = unique_id
        self.name = tournament_name
        self.location = tournament_location
        self.start = start_date
        self.end = end_date
        self.rounds = rounds
        self.time_control = tournament_time_control
        self.description = tournament_description
        self.round_to_play = round_to_play
        self.players = players
        self.matchs = matchs

        self.TOURNAMENTS.append(self)

    def serialized_tournament(self):
        serial_tournament = {
            'ID': self.unique_id,
            'Nom': self.name,
            'Lieu': self.location,
            'Date_de_debut': self.start,
            'Date_de_fin': self.end,
            'Nombre_de_rounds': self.rounds,
            'Time_control': self.time_control,
            'Description': self.description,
            'Round_a_jouer': self.round_to_play,
            'Joueurs': self.players,
            'Matchs': self.matchs
        }

        return serial_tournament

    def save_matchs(self, list_of_matchs):
        self.matchs = list_of_matchs

    def update_round(self):
        self.round_to_play += 1

    def return_all_matchs(self):
        return self.matchs

    def return_player(self, player_id):
        for player in self.players:
            if player['ID'] == player_id:
                return player

    def return_round_to_play(self, round_to_play):
        return self.matchs[round_to_play - 1]

    @classmethod
    def return_tournament_with_id(cls, id_number):
        for tournament in cls.TOURNAMENTS:
            if id_number == tournament.unique_id:
                return tournament

    @classmethod
    def return_all_tournaments(cls):
        return cls.TOURNAMENTS

    @classmethod
    def return_all_serialized_tournament(cls):
        for tournament in cls.TOURNAMENTS:
            serial_tournament = tournament.serialized_tournament()
            cls.SERIALIZED_TOURNAMENTS.append(serial_tournament)

        return cls.SERIALIZED_TOURNAMENTS
