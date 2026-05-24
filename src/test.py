import time

t0 = time.perf_counter()

from src.db import load_players
from src.similarity import get_similar_players

t1 = time.perf_counter()
print(f"Imports done ({t1 - t0:.3f}s)")

print(get_similar_players("E. Haaland"))

t2 = time.perf_counter()
print(f"Similar players found ({t2 - t1:.3f}s)")