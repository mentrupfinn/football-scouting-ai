import streamlit as st

from src.db import load_player_names


st.title("⚽ Football Scouting AI")

# alle Spielernamen laden
player_names = load_player_names()

selected_player = st.selectbox(
    "Choose a player:",
    player_names
)