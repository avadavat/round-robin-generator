import pandas as pd
from datetime import datetime, timedelta


def generate_times(matchup_df: pd.DataFrame, tournament_start_time, game_duration, game_stagger):
    time_df = pd.DataFrame(index=matchup_df.index, columns=matchup_df.columns)
    if game_stagger == 0:
        for round_num in range(time_df.shape[0]):
            round_key = 'Round ' + str(round_num + 1)
            match_time = tournament_start_time + timedelta(minutes=(game_duration*round_num))
            time_df.loc[round_key, :] = match_time.time().strftime('%H:%M%p')
        return time_df
    else:
        #TODO: Implement
        pass