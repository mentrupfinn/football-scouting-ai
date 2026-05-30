import streamlit as st

from src.db import *
from src.charts import *

# Load in dataframes
players_general_info, players_stats = import_players()

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])
top.title("Football Manager Scouting")

st.divider()

left, middle, right = st.columns([4, 3, 6])

with left:
    selected_name = st.selectbox("", players_general_info["Name"], label_visibility="collapsed")
    selected_player_general_info = players_general_info[players_general_info["Name"] == selected_name].iloc[0]
    selected_player_stats = players_stats[players_general_info["Name"] == selected_name].iloc[0]

    general = st.container(border = True)

    with general:
        for stat in ["Verein", "Nation", "Position", "Alter", "Größe", "Gewicht", "Gehalt", "Transferwert", "Einsätze", "Spielminuten"]:
            st.write(f"{stat}: {selected_player_general_info[stat]}")

with middle:
    pos = st.container(border = True)

    with pos:
        fig = plot_positions(selected_player_general_info)
        st.pyplot(fig)

with right:
    available_groups = get_valid_position_groups(selected_player_general_info)
    comparison_group = st.pills("",
        options=available_groups,
        default=available_groups[0],
        required = True
    )