from src.statics import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

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

def radar(player_name, df, features, comparison_group):
    position_cols = POSITION_GROUPS[comparison_group]
    df = df[df[position_cols].any(axis=1)]

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

    return fig

def get_valid_position_groups(player_row):

    valid_groups = []

    for group_name, positions in POSITION_GROUPS.items():

        # prüft ob irgendeine Positionsspalte True ist
        if player_row[positions].any():
            valid_groups.append(group_name)

    return valid_groups