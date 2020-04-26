import random

import pandas as pd


def apply_offset(p, n, o):
    if p == 1:
        return 1
    # Take the list of players 1 2 3 4 5 6, with offset 2, ignore the 1
    # Start with 2 3 4 5 6, we want 4 5 6 2 3
    # Shift down to 0 1 2 3 4 (p - 2)
    # Apply the offset -2 -1 0 1 2 (p - o)
    # Scale up 2 3 4 5 6 (p + (n-1))
    # Mod by (p-1) 2 3 4 0 1
    # Shift back up: 4 5 6 2 3

    s = n - 1
    return ((p - 2 - o + s) % s) + 2


def rotate_arr(arr, n, offset):
    for i in range(len(arr)):
        arr[i] = apply_offset(arr[i], n, offset)


# Generates the matchups for n players playing the r-th round of the tournament
def generate_matchups(n, r):
    if n <= 0:
        raise Exception("Number of players must be positive")
    if r <= 0 or r >= n:
        raise Exception("Round number must be within [1,n-1]")

    # Circle method, bottom array will have more than the bottom
    top = [(x + 1) for x in range(n // 2)]
    bottom = [(x + 1) for x in range(n // 2, n)]

    # Reverse bottom
    bottom.reverse()

    # Change offsets based on round
    offset = r - 1

    # Rotate the arrays based on offset
    rotate_arr(top, n, offset)
    rotate_arr(bottom, n, offset)

    # Match players
    matchups = []
    for i in range(len(top)):
        matchups.append((top[i], bottom[i]))
    # Add bye player
    if len(bottom) > len(top):
        matchups.append((bottom[len(bottom) - 1], None))

    return matchups


# Takes a list of player names and returns the matchups as a pandas data frame
def generate_player_matchups(num_rounds, players):
    # Randomly shuffle the player list
    random.shuffle(players)
    num_players = len(players)

    # Create a dataframe to store the output.
    game_cols = ["Game " + str(game_num) for game_num in range(1, num_players // 2 + 1)]
    bye_key = "Bye"
    if num_players % 2 == 1:
        game_cols.append(bye_key)
    matchup_df = pd.DataFrame(
        index=["Round " + str(i) for i in range(1, num_rounds + 1)], columns=game_cols
    )

    # Generate matchups for each round
    for r in range(1, num_rounds + 1):
        round_key = "Round " + str(r)
        matchups = generate_matchups(num_players, r)
        for i in range(len(matchups)):
            m = matchups[i]
            if m[1] is None:
                # Bye
                matchup_df.loc[round_key, bye_key] = players[m[0] - 1]
                continue
            m_str = players[m[0] - 1] + " vs. " + players[m[1] - 1]
            game_key = "Game " + str(i + 1)
            matchup_df.loc[round_key, game_key] = m_str

    return matchup_df
