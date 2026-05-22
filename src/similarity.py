import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

FEATURES = ["pace", "shooting", "passing", "dribbling", "defending", "physical"]


def get_similar_players(df, player_name, top_n=5):
    X = df[FEATURES].values

    # Zielspieler finden
    player_row = df[df["name"] == player_name]

    if player_row.empty:
        raise ValueError(f"{player_name} nicht gefunden")

    player_vector = player_row[FEATURES].values

    # nur Zielspieler gegen alle vergleichen
    similarities = cosine_similarity(player_vector, X)[0]

    df = df.copy()
    df["similarity"] = similarities

    # sich selbst entfernen
    df = df[df["name"] != player_name]

    return df.sort_values(
        "similarity",
        ascending=False
    )[["name", "club", "position", "similarity"]].head(top_n)