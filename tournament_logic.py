import random
import collections
import pandas as pd
import time
from argparse import ArgumentParser
from generate_matchups import generate_matchups
from mike_round_robin import default_scramble

random.seed(420)

# Prevent pandas from truncating output
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


class ChessTournament:
    def __init__(self, player_list):
        # List of players in the tournament
        self.players = player_list
        # How long each game takes to play
        self.game_duration = 0

    def create_matchups_2(self, num_rounds):
        # Randomly shuffle the player list
        players = self.players.copy()
        random.shuffle(players)
        n = len(players)

        start = time.perf_counter()
        # Generate matchups for each round
        for r in range(1, num_rounds + 1):
            print("-~-~- Round {0} -~-~-".format(r))
            matchups = generate_matchups(n, r)
            for m in matchups:
                print("{0} vs. {1}".format(players[m[0] - 1], players[m[1] - 1]))
        fin = time.perf_counter()
        print(f"Ran in  {fin - start:0.4f} seconds")

        # Round Robin alternate algorithm
        start = time.perf_counter()
        output = default_scramble(3, players, n)
        print(output)
        fin = time.perf_counter()
        print(f"Ran in {fin - start:0.4f} seconds")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--players_filename",
        dest="players_filename",
        help="filename containing list of players (one per line)",
        metavar="PLAYERS_FILENAME",
    )
    parser.add_argument(
        "-a",
        "--alternate_matcher",
        dest="alternate_matcher",
        help="use the alernate matching algorithms",
        action="store_true"
    )
    args = parser.parse_args()
    print(args)
    with open(args.players_filename) as f:
        players = [line.strip() for line in f]
    ct = ChessTournament(players)
    print(args)
    if args.alternate_matcher:
        ct.create_matchups_2(3)
