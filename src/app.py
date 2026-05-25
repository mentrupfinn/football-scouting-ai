import streamlit as st

from src.db import load_players
from src.similarity import get_similar_players


st.title("⚽ Football Scouting AI")

# alle Spielernamen laden
df = load_players(limit=5000)   # erstmal begrenzen für schnelleren Start
player_names = sorted(df["name"].unique())

selected_player = st.selectbox(
    "Choose a player:",
    player_names
)

top_n = st.slider(
    "How many similar players?",
    1,
    10,
    5
)

if st.button("Find Similar Players"):
    results = get_similar_players(
        selected_player,
        top_n=top_n
    )

    st.subheader("Most similar players")
    st.dataframe(results)