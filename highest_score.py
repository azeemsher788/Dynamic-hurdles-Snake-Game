import pandas as pd

data = pd.read_csv("highest.csv")


def update_score(player_name, score):
    updated_data = {"PlayerName":[player_name], "HighestScore":[score]}
    df = pd.DataFrame(updated_data)
    df.to_csv("highest.csv", index=False)


highest_score = data['HighestScore'].values[0]



