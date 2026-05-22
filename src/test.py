from src.db import load_players
from src.similarity import get_similar_players

df = load_players()

print(get_similar_players(df, "J. Kimmich"))