import collections
import random
import time
from datetime import datetime
from enum import Enum

import pandas as pd
from round_robin_generator.generate_matchups import generate_player_matchups
from round_robin_generator.mike_round_robin import default_scramble

# random.seed(420)
random.seed(datetime.now())

# Prevent pandas from truncating output
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


class MatchupImplementation(Enum):
    CIRCLE = "CIRCLE"
    DEFAULT_SCRAMBLE = "DEFAULT_SCRAMBLE"


class RoundRobinGenerator:
    """
    :type implementation: MatchupImplementation
    :param implementation: Sets the algorithm used to generate the round robin matchups. Default is the Circle method.
    """

    def __init__(self, matchup_implementation=MatchupImplementation.DEFAULT_SCRAMBLE):
        pass

    def create_matchups(self, player_list, num_rounds):
        return {
            MatchupImplementation.CIRCLE: create_matchups_circle(
                player_list, num_rounds
            ),
            MatchupImplementation.DEFAULT_SCRAMBLE: create_matchups_alternate(
                player_list, num_rounds
            ),
        }[matchup_implementation]

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
