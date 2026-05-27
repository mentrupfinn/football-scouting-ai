import streamlit as st

from src.db import *
from src.charts import *

shooting_features = [
    "xg/90",
    "xg-ohn11/90",
    "tor/90",
    "sch/90",
    "sat/90",
    "xg/schuss",
    "fernschüsse/90"
]

passing_features = [
    "xa/90",          # expected assists → Chance creation
    "vorl/90",        # key passes / assists prep
    "pr_pässe/90",    # progressive passes
    "e_pä/90",        # passes into final third (vermutlich)
    "entp(s)/90",     # passes into penalty area / dangerous zone
    "ps_a/90",        # pass attempts (volumen)
    "ps_v/90",
    "ch/90"
]

crossing_features = [
    "ang_fla/90",
    "ent_kopf/90",
    "vers_fla/90",
    "kopf_g/90",
    "kop_v/90"
]

possession_features = [
    "ballgew/90",
    "ballverl/90",
    "drb/90",
    "sprints/90",
    "lauf/90"
]

defensive_features = [
    "abb/90",
    "ent_zwk/90",
    "blk/90",
    "klär/90",
    "zwk/90"
]

goalkeeping_features = [
    "xg_verh/90",
    "gtor/90",
    "zu0/90",
    "paraden/90"
]

Rest = [
    "prserf/90",
    "prsv/90",
    "vek/90"
]

POSITION_GROUPS = {
    "TW": {"TW"},
    "IV": ["D (C)", "DC", "D"],
    "AV": ["D (L)", "D (R)", "DL", "DR", "WBL", "WBR"],
    "DM": ["DM"],
    "ZM": ["M", "MC"],
    "OM": ["AM", "AMC", "OM"],
    "Flügel": ["AM (L)", "AM (R)", "AML", "AMR"],
    "ST": ["ST"]
}

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])

top.title("⚽ Football Scouting AI")

# alle Spielernamen laden
player_names = load_player_names()

selected_player = top.selectbox(
    "Choose a player:",
    player_names
)

player_df = get_player(selected_player)
player = player_df.iloc[0]


st.divider()

left, middle, right = st.columns([4, 3, 6])

with left:
    st.header(selected_player)
    gen = st.container(border = True)

    with gen:
        st.write(f"Verein: {player['verein']}")
        st.write(f"Nation: {player['nation']}")
        st.write(f"Position: {player['position']}")
        st.write(f"Alter: {int(player['alter'])}")
        st.write(f"Größe: {player['größe']}")
        st.write(f"Gewicht: {player['gewicht']}")
        st.write(f"Gehalt: {player['gehalt']}")
        st.write(f"Transferwert: {player['transferwert']}")
        st.write(f"Einsätze: {player['eins']}")
        st.write(f"Spielminuten: {player['min_']}")

with middle:
    pos = st.container(border = True)

    with pos:
        fig = plot_positions(get_player(selected_player).iloc[0])
        st.pyplot(fig)

with right:

    toggle, chart = st.columns([1,7])

    with toggle:
        st.write("")
        st.write("")
        comparison_group = st.pills("",
            options=["Alle", "TW", "IV", "AV", "DM", "ZM", "OM", "Flügel", "ST"],
            default="ST"
        )

    with chart:

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Schießen", "Passen", "Flanken",
                                                            "Ballbesitz", "Verteidigung", "Torwart", "Rest"])

        with tab1:
            radar(selected_player, shooting_features)
        
        with tab2:
            radar(selected_player, passing_features)

        with tab3:
            radar(selected_player, crossing_features)

        with tab4:
            radar(selected_player, possession_features)

        with tab5:
            radar(selected_player, defensive_features)

        with tab6:
            radar(selected_player, goalkeeping_features)

        with tab7:
            radar(selected_player, Rest)

st.divider()

if st.button("Reload database"):
    import_players()