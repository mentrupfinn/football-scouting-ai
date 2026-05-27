import streamlit as st

from src.db import *
from src.charts import *
from src.statics import *

# Load in dataframes
players = import_players()
player_names = players["name"]

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])
top.title("⚽ Football Scouting AI")
selected_name = top.selectbox("Choose a player:", player_names)
selected_player = players[players["name"] == selected_name].iloc[0]

st.divider()

left, middle, right = st.columns([4, 3, 6])

with left:
    st.header(selected_name)
    gen = st.container(border = True)

    with gen:
        st.write(f"Verein: {selected_player['verein']}")
        st.write(f"Nation: {selected_player['nation']}")
        st.write(f"Position: {selected_player['position']}")
        st.write(f"Alter: {int(selected_player['alter'])}")
        st.write(f"Größe: {selected_player['größe']}")
        st.write(f"Gewicht: {selected_player['gewicht']}")
        st.write(f"Gehalt: {selected_player['gehalt']}")
        st.write(f"Transferwert: {selected_player['transferwert']}")
        st.write(f"Einsätze: {selected_player['eins']}")
        st.write(f"Spielminuten: {selected_player['min_']}")

with middle:
    pos = st.container(border = True)

    with pos:
        fig = plot_positions(selected_player)
        st.pyplot(fig)

with right:

    toggle, chart = st.columns([1,7])

    with toggle:
        st.write("")
        st.write("")
        comparison_group = st.pills("",
            options=["Alle", "TW", "IV", "AV", "DM", "ZM", "OM", "Flügel", "ST"],
            default="Alle"
        )

    with chart:

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Schießen", "Passen", "Flanken",
                                                            "Ballbesitz", "Verteidigung", "Torwart", "Rest"])

        with tab1:
            st.plotly_chart(radar(selected_name, players, shooting_features))
        
        with tab2:
            st.plotly_chart(radar(selected_name, players, passing_features))

        with tab3:
            st.plotly_chart(radar(selected_name, players, crossing_features))

        with tab4:
            st.plotly_chart(radar(selected_name, players, possession_features))

        with tab5:
            st.plotly_chart(radar(selected_name, players, defensive_features))

        with tab6:
            st.plotly_chart(radar(selected_name, players, goalkeeping_features))

        with tab7:
            st.plotly_chart(radar(selected_name, players, rest_features))