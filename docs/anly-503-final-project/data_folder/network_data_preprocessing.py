import numpy as np
import pandas as pd

sn_raw = pd.read_csv("SN_teambuild.csv")

all_team_build = sn_raw.groupby('gameid')['champion'].apply(list).tolist()

# ideal data format
# champion_1 | champion_2 | weight

# key: (champion_1, champion_2), value: counts

# all_team_build = sn_raw.groupby('gameid')['champion'].apply(list).tolist()
# this = all_team_build[0]



def get_champion_pair_counts(all_team_build_list):

    champ_pairs = {}

    for team in all_team_build_list:
        while(len(team) > 1):
            champion_1 = team[0]
            for champion_2 in team[1:]:
                print("champion_1 is", champion_1)
                print("champion 2 is", champion_2)
                print("remaining champions are", this)
                temp = [champion_1, champion_2]
                temp.sort()
                pair = tuple(temp)
                print(pair)
                if pair in champ_pairs:
                    champ_pairs[pair] += 1
                else:
                    champ_pairs[pair] = 1
            team.remove(champion_1)

    return champ_pairs

sn_champ_pairs = get_champion_pair_counts(all_team_build)
champ_pair_df = pd.DataFrame.from_dict(sn_champ_pairs, orient='index')

champ_pair_df.reset_index