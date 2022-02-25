from Views.Input import return_tournament_id, display_results, continue_tournament
from Views.Output import no_tournament_find, display_match, display_results_title, \
    tournament_is_ending
from Models.Tournament import Tournament


def get_tournament_with_id():

    tournament_id = return_tournament_id()
    if tournament_id == 0:
        return
    tournament = Tournament.return_tournament_with_id(tournament_id)
    if not tournament:
        no_tournament_find()
        return get_tournament_with_id()
    else:
        return tournament


def run_round(tournament):

    if tournament.round_to_play >= 5:
        tournament_is_ending(tournament.players)
        return
    list_of_matchs = tournament.return_round_to_play(tournament.round_to_play)
    display_match(list_of_matchs, tournament.round_to_play)
    display_results_title()
    display_results(list_of_matchs, tournament)
    if tournament.round_to_play == 4:
        tournament_is_ending(tournament.players)
        tournament.update_round()
        return
    else:
        choice = continue_tournament()
        if choice == 'O':
            tournament.update_round()
            return run_round(tournament)
        elif choice == 'N':
            tournament.update_round()
            return
