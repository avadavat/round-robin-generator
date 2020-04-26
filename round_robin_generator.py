from argparse import ArgumentParser

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
    args = parser.parse_args()
    with open(args.players_filename) as f:
        players = [line.strip() for line in f]
    num_rounds = int(args.num_rounds)
    matchup_implementation = (
        args.matchup_implementation or MatchupImplementation.DEFAULT_SCRAMBLE
    )

    rrg_default = RoundRobinGenerator(matchup_implementation=matchup_implementation)
    default_matchups = rrg_default.create_matchups(players, num_rounds)
    print(default_matchups)
