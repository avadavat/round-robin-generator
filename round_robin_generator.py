from argparse import ArgumentParser
from round_robin_generator.matchup_times import generate_times
from round_robin_generator.RoundRobinGenerator import (  # isort:skip
    MatchupImplementation,
    RoundRobinGenerator,
)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--players_filename",
        dest="players_filename",
        help="filename containing list of players (one per line)",
        metavar="PLAYERS_FILENAME",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--num_rounds",
        dest="num_rounds",
        help="number of rounds to play (0 < r < num_players)",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--matchup_implementation",
        dest="matchup_implementation",
        help="Algorithm to use to generate the random matchups",
        required=False,
    )
    parser.add_argument(
        "-t",
        "--tournament_start_time",
        dest="tournament_start_time",
        default="12:00PM",
        help="When the first game will be played. e.g. 12:00pm",
        required=False,
    )
    parser.add_argument(
        "-gd",
        "--game_duration",
        dest="game_duration",
        default='10',
        help="Game duration in minutes. e.g. 10",
        required=False,
    )
    parser.add_argument(
        "-stag",
        "--game_stagger",
        dest="game_stagger",
        default='0',
        help="Game staggering in minutes. e.g. 5",
        required=False,
    )

    args = parser.parse_args()
    with open(args.players_filename) as f:
        players = [line.strip() for line in f]
    num_rounds = int(args.num_rounds)
    matchup_implementation = (
            args.matchup_implementation or MatchupImplementation.CIRCLE
    )
    rrg_default = RoundRobinGenerator(tournament_start_time=args.tournament_start_time,
                                      game_duration=args.game_duration, game_stagger=args.game_stagger,
                                      matchup_implementation=matchup_implementation)
    default_matchups = rrg_default.create_matchups(players, num_rounds)
    print(default_matchups)
    default_times = generate_times(default_matchups, rrg_default.tournament_start_time, rrg_default.game_duration,
                                   rrg_default.game_stagger)
    print(default_times)
