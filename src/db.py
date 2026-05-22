import pandas as pd
from sqlalchemy import create_engine

# Format:
# postgresql://user:password@host:port/database

DB_URL = "postgresql://postgres:9450@localhost:5432/scouting_db"

engine = create_engine(DB_URL)

def load_players():
    query = "SELECT * FROM players;"
    return pd.read_sql(query, engine)


if __name__ == "__main__":
    df = load_players()
    print(df.head())