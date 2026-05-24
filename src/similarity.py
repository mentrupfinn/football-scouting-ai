from sklearn.metrics.pairwise import cosine_similarity
from src.db import load_players, get_player


FEATURES = [
    "pace",
    "shooting",
    "passing",
    "dribbling",
    "defending",
    "physical"
]


def get_similar_players(player_name, top_n=5):
    # Zielspieler laden
    player_df = get_player(player_name)

    if player_df.empty:
        raise ValueError(f"{player_name} nicht gefunden")

    # Hauptposition bestimmen
    main_position = (
        player_df.iloc[0]["position"]
        .split(",")[0]
        .strip()
    )

    print(f"Searching within position group: {main_position}")

    # passende Gruppe laden
    df = load_players(position=main_position)

    X = df[FEATURES].values
    player_vector = player_df[FEATURES].values

    similarities = cosine_similarity(
        player_vector,
        X
    )[0]

    df = df.copy()
    df["similarity"] = similarities

    # Spieler selbst entfernen
    df = df[df["name"] != player_name]

    return df.sort_values(
        "similarity",
        ascending=False
    )[[
        "name",
        "club",
        "position",
        "similarity"
    ]].head(top_n)