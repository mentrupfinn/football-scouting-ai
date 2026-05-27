import pandas as pd
import streamlit as st
import plotly.graph_objects as go

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
