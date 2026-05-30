import streamlit as st

from src.db import *
from src.charts import *
from src.statics import *

from src.pca import *
from src.clustering import *
from src.feature_set_analysis import *

# Load in dataframes
players = import_players()
player_names = players["name"]

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])
top.title("Football Manager Scouting")

st.divider()

left, middle, right = st.columns([4, 3, 6])

with left:
    selected_name = st.selectbox("", player_names, label_visibility="collapsed")
    selected_player = players[players["name"] == selected_name].iloc[0]

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
        available_groups = get_valid_position_groups(selected_player)
        comparison_group = st.pills("",
            options=available_groups,
            default=available_groups[0],
            required = True
        )

    with chart:

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Schießen", "Passen", "Flanken",
                                                            "Ballbesitz", "Verteidigung", "Torwart"])

        with tab1:
            st.plotly_chart(radar(selected_name, players, shooting_features, comparison_group))
        
        with tab2:
            st.plotly_chart(radar(selected_name, players, passing_features, comparison_group))

        with tab3:
            st.plotly_chart(radar(selected_name, players, crossing_features, comparison_group))

        with tab4:
            st.plotly_chart(radar(selected_name, players, possession_features, comparison_group))

        with tab5:
            st.plotly_chart(radar(selected_name, players, defensive_features, comparison_group))

        with tab6:
            st.plotly_chart(radar(selected_name, players, goalkeeping_features, comparison_group))

st.divider()

players_sig = players[players["min_"] > 900]
players_in_group = players_sig[players[POSITION_GROUPS["ZM"]].any(axis=1)]

stats = players_in_group[ZM_FEATURES].apply(pd.to_numeric, errors="coerce")
pcts = stats.rank(pct=True)

st.plotly_chart(plot_pca(pcts, players_in_group["name"].values))

st.divider()

