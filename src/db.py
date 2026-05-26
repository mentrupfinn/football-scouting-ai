import pandas as pd
from sqlalchemy import create_engine, text

# Format:
# postgresql://user:password@host:port/database

DB_URL = "postgresql://postgres:9450@localhost:5432/scouting_db"

engine = create_engine(DB_URL)

def get_player(player_name):
    query = """
        SELECT *
        FROM players
        WHERE Name = :player_name;
    """

    return pd.read_sql(
        text(query),
        engine,
        params={"player_name": player_name}
    )

def load_player_names():
    query = "SELECT name FROM players;"

    return pd.read_sql(text(query), engine)

def load_players(position=None, limit=None):
    query = "SELECT * FROM players"

    conditions = []

    if position:
        conditions.append(f"position LIKE '%{position}%'")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    if limit:
        query += f" LIMIT {limit}"

    query += ";"

    return pd.read_sql(text(query), engine)

def import_players(csv_path="data/players_raw.csv"):
    df = pd.read_csv(csv_path,sep=";")

    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))

    df = df.drop(columns=["empf", "info"])

    df.to_sql(
        "players",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{len(df)} Spieler importiert.")

if __name__ == "__main__":
    import_players()
    df = load_players()
    print(df.head())
    print(df.columns.tolist())