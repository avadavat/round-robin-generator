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

    def create_matchups(self, num_rounds: int):
        """
        Creates the matchups that will occur in each round.
        :param num_rounds: Number of rounds in the tournament & the number of games each team will play. Constrained to
        to be at most the number of teams minus 1. (Everyone plays each other once.)
        :return: Returns a dataframe of matchups that will occur.
        """
        # Dictionary of number of matches played by each player
        player_match_count = collections.defaultdict(list)
        player_match_count[0] = self.players
        # List of all matches that will occur
        all_matches = []
        for j in range(num_rounds):
            # List of matches in the current round
            matchup_list = []
            # In case the algorithm gets stuck making duplicates
            fail_count = 0
            while len(player_match_count[j]) > 1:
                # Randomly generating a matchup
                random_idxs = random.sample(range(0, len(player_match_count[j])), 2)
                # Making sure the matchup didn't already occur
                if (
                    sorted(
                        [
                            player_match_count[j][random_idxs[0]],
                            player_match_count[j][random_idxs[1]],
                        ]
                    )
                    not in all_matches
                ):
                    matchup = [
                        player_match_count[j].pop(i)
                        for i in sorted(random_idxs, reverse=True)
                    ]
                    # Advancing the count of games played by each player
                    [player_match_count[j + 1].append(p) for p in matchup]
                    # Sorting occurs to ensure easier checking of presence of values
                    matchup_list.append(sorted(matchup))
                    all_matches.append(sorted(matchup))
                else:
                    print(
                        "This combination is a duplicate of an earlier matchup: ",
                        player_match_count[j][random_idxs[0]],
                        "vs. ",
                        player_match_count[j][random_idxs[1]],
                    )
                    fail_count += 1
                    if fail_count > 5:
                        break

            # Write the matchups for a given round to the master matchup dictionary.
            key_str = "Round" + str(j + 1)
            self.actual_matchups[key_str] = matchup_list


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
