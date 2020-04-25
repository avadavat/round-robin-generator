import pandas as pd

def default_scramble(num_rounds, players):
    num_players = len(players)
    # Create a dataframe to store the output.
    matchup_df = pd.DataFrame(index=['Round ' + str(i) for i in range(1, num_rounds + 1)],
                              columns=['Game ' + str(game_num) for game_num in
                                       range(1, num_players // 2 + 1)])

    # Generate matchups for each round via a round robin algorithm.
    for r in range(1, num_rounds + 1):
        # Setting the first matchup of the round to always include the last player.
        matchup_df.loc['Round ' + str(r), 'Game 1'] = players[r - 1] + ' vs. ' + players[-1]
        # Subsetting the remaining eligible players.
        sub_players = players[r: num_players - 1] + players[:r - 1]
        for idx in range(num_players // 2 - 1):
            match = (sub_players[idx] + ' vs. ' + sub_players[-1 - 1 * idx])
            # Writing each match to the output dataframe.
            matchup_df.loc['Round ' + str(r), 'Game ' + str(idx + 2)] = match
    return matchup_df
