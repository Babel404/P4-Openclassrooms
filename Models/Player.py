
class Player:
    PLAYERS = []
    SERIALIZED_PLAYERS = []

    def __init__(self, unique_id, first_name, last_name, date_of_birth, gender, ranking, score):
        self.id = unique_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score

        self.PLAYERS.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ID n°{self.id} - Classement actuel : {self.ranking}\n"

    def modify_ranking(self, new_ranking):
        self.ranking = new_ranking

    def serialized_player(self):
        serialized_player = {
            'ID': self.id,
            'Nom': self.first_name,
            'Prenom': self.last_name,
            'Date_de_naissance': self.date_of_birth,
            'Sexe': self.gender,
            'Classement': self.ranking,
            'Score': self.score
        }

        return serialized_player

    @classmethod
    def return_all_players(cls):
        return cls.PLAYERS

    @classmethod
    def return_player(cls, unique_id):
        for player in cls.PLAYERS:
            if unique_id == player.id:
                return player

    @classmethod
    def does_player_exist_in_db(cls, first_name, last_name):
        for player in cls.PLAYERS:
            if player.first_name == first_name and player.last_name == last_name:
                return player

    @classmethod
    def return_unique_id(cls, first_name, last_name):
        for player in cls.PLAYERS:
            if first_name == player.first_name and last_name == player.last_name:
                return player.id

    @classmethod
    def return_all_serialized_players(cls):
        for player in cls.PLAYERS:
            player_ser = player.serialized_player()
            cls.SERIALIZED_PLAYERS.append(player_ser)

        return cls.SERIALIZED_PLAYERS
