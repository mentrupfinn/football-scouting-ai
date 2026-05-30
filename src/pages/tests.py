import streamlit as st

from src.db import *
from src.feature_set_analysis import *
from src.pos_groups import *
from src.stat_groups import *

players = import_players()

st.set_page_config(layout="wide")

pad1,top,pad2 = st.columns([1,2,1])
top.title("Tests and Experiments")

st.divider()

st.write(len(filter(players,"ZM").index))

position_group = st.pills("", options = POSITION_GROUPS, default = "TW", required = True)

feature = st.pills("", options = stats, default = stats[0], required = True)

filter_zeros = st.pills("Filter zero values?", options = [True, False])

bins = st.pills("Amount of bins: ", options= [10, 50, 100])

st.pyplot(feature_hist(players, position_group, feature, bins, filter_zeros))