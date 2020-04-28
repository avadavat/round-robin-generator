import pandas as pd
from datetime import timedelta


def generate_times(matchup_df: pd.DataFrame, tournament_start_time, game_duration, game_stagger):
    time_df = pd.DataFrame(index=matchup_df.index, columns=matchup_df.columns)
    if game_stagger == 0:
        for round_num in range(time_df.shape[0]):
            round_key = 'Round ' + str(round_num + 1)
            match_time = tournament_start_time + timedelta(minutes=(game_duration * round_num))
            time_df.loc[round_key, :] = match_time.strftime('%I:%M%p')
        return time_df
    else:
        """
        # Given the algorithm, at worst every player can play every (game duration + stagger time)
        # This is b/c your opponent begins play one stagger count after you at the latest.
        """
        for round_num in range(time_df.shape[0]):
            round_key = 'Round ' + str(round_num + 1)
            default_spread = [tournament_start_time + timedelta(minutes=game_num * game_stagger) for game_num in
                              range(time_df.shape[1])]
            match_times = [
                (def_time + timedelta(minutes=((game_duration + game_stagger) * round_num))).strftime('%I:%M%p') for
                def_time in default_spread]
            time_df.loc[round_key, :] = match_times
        return time_df
