import pandas as pd
from sqlalchemy import create_engine, text
import re
from itertools import product

# Format:
# postgresql://user:password@host:port/database

DB_URL = "postgresql://postgres:9450@localhost:5432/scouting_db"

engine = create_engine(DB_URL)

def get_player(player_name):
    query = """
        SELECT *
        FROM players
        WHERE name = :player_name;
    """

    return pd.read_sql(
        text(query),
        engine,
        params={"player_name": player_name}
    )

def load_player_names():
    query = "SELECT name FROM players;"

    return pd.read_sql(text(query), engine)

def load_players(position=None, significant = True, limit=None):
    query = "SELECT * FROM players"

    conditions = []

    if significant:
        conditions.append("min_ > 900")

    if position:
        conditions.append(f"position LIKE '%{position}%'")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    if limit:
        query += f" LIMIT {limit}"

    query += ";"

    return pd.read_sql(text(query), engine)

def import_players(path="data/players_raw.html"):
    df = pd.read_html(path, encoding="utf-8")[0]

    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(".", "_"))

    df = df.drop(columns=["empf", "info"])

    df = df.replace("-", 0.0)

    df["min_"] = (
        df["min_"]
        .str.replace(",", "", regex=False)
        .replace("-", 0)
    )

    df["lauf/90"] = (df["lauf/90"].str.replace("km", "", regex=False))

    df["min_"] = pd.to_numeric(df["min_"], errors="coerce").astype("Int64")

    pos_matrix = df["position"].apply(encode_position_matrix).apply(pd.Series)
    df = pd.concat([df, pos_matrix], axis=1)

    df.to_sql(
        "players",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{len(df)} Spieler importiert.")

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

POSITIONS = [
    "TW(Z)",
    "V(L)", "V(Z)", "V(R)",
    "FV(L)", "DM(Z)", "FV(R)",
    "M(L)", "M(Z)", "M(R)",
    "OM(L)", "OM(Z)", "OM(R)",
    "ST(Z)"
]

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

if __name__ == "__main__":
    import_players()