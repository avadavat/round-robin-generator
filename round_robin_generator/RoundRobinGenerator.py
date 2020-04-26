import collections
import random
import time
from datetime import datetime

import pandas as pd
from round_robin_generator.generate_matchups import generate_player_matchups
from round_robin_generator.mike_round_robin import default_scramble

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
