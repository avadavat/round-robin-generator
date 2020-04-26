import collections
import random
import time
from argparse import ArgumentParser
from datetime import datetime

import pandas as pd
from generate_matchups import generate_player_matchups
from mike_round_robin import default_scramble

# random.seed(420)
random.seed(datetime.now())

# Prevent pandas from truncating output
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


class RoundRobinGenerator:
    def __init__(self):
        pass

    def create_matchups_circle(self, player_list, num_rounds):
        # Create matchups using the circle method
        start = time.perf_counter()

        players = player_list.copy()
        output = generate_player_matchups(num_rounds, players)
        print(output)

        fin = time.perf_counter()
        print("Ran in  {0:0.4f} seconds".format(fin - start))

    def create_matchups_alternate(self, player_list, num_rounds):
        # Round Robin alternate algorithm
        start = time.perf_counter()

        players = player_list.copy()
        output = default_scramble(num_rounds, players)
        print(output)

        fin = time.perf_counter()
        print("Ran in {0:0.4f} seconds".format(fin - start))


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

    ct = RoundRobinGenerator()
    ct.create_matchups_circle(players, num_rounds)
    ct.create_matchups_alternate(players, num_rounds)
