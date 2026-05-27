import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from src.db import load_players

def radar(player_name, features):
    df = load_players()

    df_stats = df[features].apply(pd.to_numeric, errors="coerce")

    player_stats = df_stats[df["name"] == player_name].iloc[0].tolist()

    df_pct = df_stats.rank(pct=True)

    player_pct = df_pct[df["name"] == player_name].iloc[0].tolist()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=player_pct + [player_pct[0]],
        theta=features + [features[0]],
        fill='toself',
        name = "",
        customdata = player_stats + [player_stats[0]],
        hovertemplate=
            "<b>%{theta}</b><br>" +
            "Value: %{customdata:.2f}<br>" +
            "Percentile: %{r:.0%}<br>" +
            "<extra></extra>"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                showline = False,
                showticklabels = False,
                ticks = ""
            ),
            bgcolor='rgba(0,0,0,0)'
        )
    )

    st.plotly_chart(fig)

def plot_positions(player):
    fig, ax = plt.subplots(figsize=(4, 5), facecolor='none')

    # Pitch background
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 6)
    ax.axis("off")

    for pos, (x, y) in POSITION_LAYOUT.items():

        is_active = player.get(pos, False)

        color = "green" if is_active else "lightgray"

        if is_active:
            ax.scatter(
                x, y,
                s=500,
                facecolors="green",
                edgecolors="black",
                linewidths=1
            )
        else:
            ax.scatter(
                x, y,
                s=100,
                facecolors="none",      # <- leer (wichtig!)
                edgecolors="gray",      # <- nur Outline
                linewidths=1.5
            )

    return fig

POSITION_LAYOUT = {
    "TW(Z)": (0, 0),

    "V(L)": (-2, 1),
    "V(Z)": (0, 1),
    "V(R)": (2, 1),

    "FV(L)": (-2, 2),
    "DM(Z)": (0, 2),
    "FV(R)": (2, 2),

    "M(L)": (-2, 3),
    "M(Z)": (0, 3),
    "M(R)": (2, 3),

    "OM(L)": (-2, 4),
    "OM(Z)": (0, 4),
    "OM(R)": (2, 4),

    "ST(Z)": (0, 5)
}