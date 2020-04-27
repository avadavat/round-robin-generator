import collections
import random
from datetime import datetime
from enum import Enum

import pandas as pd

from round_robin_generator.matchup_generation_circle import generate_player_matchups
from round_robin_generator.matchup_generation_default_scramble import default_scramble
from round_robin_generator.decorators import time_performance

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
        self.matchup_implementation = matchup_implementation

    @time_performance
    def create_matchups(self, player_list, num_rounds):
        players = player_list.copy()

        if self.matchup_implementation == MatchupImplementation.CIRCLE.name:
            return generate_player_matchups(num_rounds, players)
        else:
            return default_scramble(num_rounds, players)
