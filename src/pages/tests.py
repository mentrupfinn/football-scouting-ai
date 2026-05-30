import streamlit as st

from src.db import *
from src.feature_set_analysis import *
from src.pos_groups import *
from src.pos_groups import POSITION_GROUPS

players = import_players()

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])
top.title("Tests and Experiments")

st.divider()

position_group = st.pills("", options = POSITION_GROUPS, default = "TW", required = True)

st.pyplot(pos_var(players, position_group))

st.pyplot(plot_gmm(filter(players,"TW")["Lauf/90"]))