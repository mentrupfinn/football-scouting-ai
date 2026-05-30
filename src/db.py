import pandas as pd
import re
from itertools import product
import streamlit as st

from src.statics import POSITIONS
from src.stat_groups import stats

@st.cache_data(show_spinner="Lade Spielerdaten...")
def import_players(path="data/players_raw.html"):
    players = pd.read_html(path, encoding="utf-8")[0] # Rohdatei einlesen

    players = players.drop(columns=["Empf", "Info"]) # unnötige Spalten entfernen

    # Spalten lesbarer benennen

    players = players.rename(columns={
        "Eins" : "Einsätze",
        "Min." : "Spielminuten"
    })

    players = players.replace("-", 0.0) # Keine leeren Einträge

    players["Spielminuten"] = pd.to_numeric(players["Spielminuten"], errors="coerce").astype("Int64")

    players = players[players["Spielminuten"] > 900] # Nur statistisch relevante Einträge

    players["Lauf/90"] = (players["Lauf/90"].str.replace("km", "", regex=False))

    players[stats] = players[stats].replace(",", ".", regex=True)

    players[stats] = players[stats].apply(
        pd.to_numeric,
        errors="coerce"
    )

    # Positionen-String auftrennen in Positionsmatrix
    pos_matrix = players["Position"].apply(encode_position_matrix).apply(pd.Series)
    players = pd.concat([players, pos_matrix], axis=1)

    return players

def parse_fm_position(pos_string):
    pos_string = str(pos_string)

    # 1. split by comma → alternative position blocks
    blocks = [b.strip() for b in pos_string.split(",")]

    results = []

    for block in blocks:

        # 2. extract width (L/R/Z)
        width_match = re.search(r"\((.*?)\)", block)
        width = list(width_match.group(1)) if width_match else ["Z"]

        # 3. remove parentheses content
        roles_part = re.sub(r"\(.*?\)", "", block).strip()

        # 4. split roles by "/"
        roles = roles_part.split("/")

        # 5. combine roles × widths
        for r, w in product(roles, width):
            results.append((r.strip(), w))

    return results

def encode_position_matrix(pos_string):
    pairs = parse_fm_position(pos_string)

    features = {}

    for pos in POSITIONS:
        features[pos] = False

    for p, w in pairs:
        key = f"{p}({w})"
        if key in features:
            features[key] = True

    return features