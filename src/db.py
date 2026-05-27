import pandas as pd
import re
from itertools import product
import streamlit as st

from src.statics import POSITIONS

@st.cache_data(show_spinner="Lade Spielerdaten...")
def import_players(path="data/players_raw.html"):
    df = pd.read_html(path, encoding="utf-8")[0]

    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(".", "_"))

    df = df.drop(columns=["empf", "info"])

    df = df.replace("-", 0.0)

    df["lauf/90"] = (df["lauf/90"].str.replace("km", "", regex=False))

    df["min_"] = pd.to_numeric(df["min_"], errors="coerce").astype("Int64")

    pos_matrix = df["position"].apply(encode_position_matrix).apply(pd.Series)
    df = pd.concat([df, pos_matrix], axis=1)

    return df

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