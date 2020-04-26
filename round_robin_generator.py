from argparse import ArgumentParser

from round_robin_generator.tournament_logic import RoundRobinGenerator

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
    args = parser.parse_args()
    with open(args.players_filename) as f:
        players = [line.strip() for line in f]
    num_rounds = int(args.num_rounds)

    rrg = RoundRobinGenerator()
    rrg.create_matchups_circle(players, num_rounds)
    rrg.create_matchups_alternate(players, num_rounds)
