import pandas as pd
import random


def default_even(num_rounds, players, num_players, reshuffle_excess=True):
    # Create a dataframe to store the output.
    matchup_df = pd.DataFrame(
        index=["Round " + str(i) for i in range(1, num_rounds + 1)],
        columns=[
            "Game " + str(game_num) for game_num in range(1, num_players // 2 + 1)
        ],
    )

    # Generate matchups for each round via a round robin algorithm.
    loop_count = -1
    for r in range(0, num_rounds):
        # Keeping track of the number of full robins
        if r % (num_players - 1) == 0:
            # Reshuffling every time there is a full robin if the user desires
            if reshuffle_excess:
                random.shuffle(players)
            loop_count += 1
        r = (r % (num_players - 1))

        # Setting the first matchup of the round to always include the last player.
        matchup_df.loc["Round " + str(r + 1 + (num_players - 1) * loop_count), "Game 1"] = (
                players[r] + " vs. " + players[-1]
        )
        # Subsetting the remaining eligible players.
        sub_players = players[r + 1: num_players - 1] + players[: r]
        for idx in range(num_players // 2 - 1):
            match = sub_players[idx] + " vs. " + sub_players[-1 - 1 * idx]
            # Writing each match to the output dataframe.
            matchup_df.loc["Round " + str(r + 1 + (num_players - 1) * loop_count), "Game " + str(idx + 2)] = match
    return matchup_df


def default_scramble(num_rounds, players, reshuffle_excess=True):
    # Initial shuffling of the player list
    random.shuffle(players)
    num_players = len(players)

    if num_players <= 0:
        raise Exception("Number of players must be positive.")
    if num_rounds <= 0:
        raise Exception("Round number must be within [1,n-1]")
    if num_players % 2 !=0:
        raise Exception('Number of teams must be even.')

    if num_players % 2 == 0:
        return default_even(num_rounds, players, num_players, reshuffle_excess)

    else:
        pass