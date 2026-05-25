import streamlit as st

from src.db import load_player_names
from src.similarity import get_similar_players


st.title("⚽ Football Scouting AI")

# alle Spielernamen laden
player_names = load_player_names()

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