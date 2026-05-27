import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from src.db import load_players

def radar(player_name, features):
    df = load_players()

    df_shoot = df[features].apply(pd.to_numeric, errors="coerce")
    df_z = (df_shoot - df_shoot.mean()) / df_shoot.std()

    player = df_z[df["name"] == player_name].iloc[0]

    categories = features.copy()

    values = player.values.tolist()

    # Kreis schließen
    values = values + values[:1]

    N = len(categories)

    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    angles = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True), facecolor="none")

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color="white")

    ax.tick_params(axis = 'x', pad=15)
    ax.tick_params(colors="white")

    ax.set_facecolor("none")
    fig.set_facecolor("none")

    st.pyplot(fig)
