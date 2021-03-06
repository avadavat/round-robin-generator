import collections
import random
from datetime import datetime
from enum import Enum

import pandas as pd

from round_robin_generator.matchup_generation_circle import generate_player_matchups
from round_robin_generator.decorators import time_performance

random.seed(datetime.now())

# Prevent pandas from truncating output
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


class MatchupImplementation(Enum):
    CIRCLE = "CIRCLE"


class RoundRobinGenerator:
    """
    :type implementation: MatchupImplementation
    :param implementation: Sets the algorithm used to generate the round robin matchups. Default is the Circle method.
    """

    def __init__(self, tournament_start_time, game_duration, game_stagger,
                 matchup_implementation=MatchupImplementation.CIRCLE):
        self.tournament_start_time = datetime.strptime(tournament_start_time, '%H:%M%p')
        self.game_duration = int(game_duration)
        self.game_stagger = int(game_stagger)
        self.matchup_implementation = matchup_implementation

    @time_performance
    def create_matchups(self, player_list, num_rounds):
        players = player_list.copy()

        if self.matchup_implementation == MatchupImplementation.CIRCLE.name:
            return generate_player_matchups(num_rounds, players)

