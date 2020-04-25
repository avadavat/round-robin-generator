import random
import collections
import pandas as pd
from argparse import ArgumentParser
from generate_matchups import generate_matchups

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
        # Mathchups that will be played.
        self.actual_matchups = dict.fromkeys(["Round1", "Round2", "Round3"], [])

    def create_matchups_2(self, num_rounds):
        # Randomly shuffle the player list
        players = self.players.copy()
        random.shuffle(players)
        n = len(players)

        # Generate matchups for each round
        for r in range(1, num_rounds + 1):
            print("-~-~- Round {0} -~-~-".format(r))
            matchups = generate_matchups(n, r)
            for m in matchups:
                print("{0} vs. {1}".format(players[m[0]-1], players[m[1]-1]))


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

    with open(args.players_filename) as f:
        players = [line.strip() for line in f]
    ct = ChessTournament(players)
    if args.alternate_matcher:
        ct.create_matchups_2(3)
    else:
        ct.create_matchups(3)
        # Outputting the df of games to be played.
        matchup_df = pd.DataFrame.from_dict(ct.actual_matchups, orient="index")
        matchup_df.columns = ["Game " + str(i + 1) for i in range(len(matchup_df.columns))]
        # matchup_df.to_excel('Chess_Matchups.xlsx')
        print(matchup_df)
