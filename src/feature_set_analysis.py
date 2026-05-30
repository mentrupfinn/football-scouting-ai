import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from sklearn.mixture import GaussianMixture

from src.pos_groups import *
from src.stat_groups import stats

# Positionsspezifische Mittelwerte 

def pos_mean_diff(players, position_group):
    position_players = filter(players, position_group)

    overall_means = players[stats].mean()
    means = position_players[stats].mean()

    values = means / overall_means

    farben = [
        "yellow" if x > 1.2  
        else "green" if x > 1
        else "blue" 
        for x in values.values]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        values.index,
        values.values,
        color = farben
    )

    ax.set_title(position_group)

    plt.xticks(rotation=90)

    plt.axhline(1.0, color="green", linestyle="--")
    plt.axhline(1.2, color="yellow", linestyle="--")

    return fig

def pos_var_diff(players, position_group):
    position_players = filter(players, position_group)

    overall_vars = players[stats].var()
    vars = position_players[stats].var()

    values = vars / overall_vars

    farben = [
        "yellow" if x > 1.2  
        else "green" if x > 1
        else "blue" 
        for x in values.values]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        values.index,
        values.values,
        color = farben
    )

    ax.set_title(position_group)

    plt.xticks(rotation=90)

    plt.axhline(1.0, color="green", linestyle="--")
    plt.axhline(1.2, color="yellow", linestyle="--")

    return fig

def pos_var(players, position_group):
    position_stats = filter(players, position_group)[stats]

    position_stats = (position_stats - players[stats].mean())/players[stats].std()

    values = position_stats.std()

    farben = [
        "yellow" if x > 1.2  
        else "green" if x > 1
        else "blue" 
        for x in values.values]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        values.index,
        values.values,
        color = farben
    )

    ax.set_title(position_group)

    plt.xticks(rotation=90)

    plt.axhline(1.0, color="green", linestyle="--")
    plt.axhline(1.2, color="yellow", linestyle="--")

    return fig

def corr_heatmap(players, position_group):
    position_stats = filter(players, position_group)[stats]
    corr = position_stats.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1
    )

    fig.update_layout(
        title="Feature Correlation Heatmap",
        xaxis_title="Features",
        yaxis_title="Features",
        width=1600,
        height=1100
    )

    return fig

def plot_gmm(feature, k=2):

    # Daten vorbereiten
    X = feature.dropna().values.reshape(-1, 1)

    # Modell fitten
    gmm = GaussianMixture(n_components=k, random_state=42)
    gmm.fit(X)

    # x-Werte für Kurve
    x = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)

    # GMM-Dichte
    density = np.exp(gmm.score_samples(x))

    # Figure erzeugen
    fig, ax = plt.subplots()

    # Histogramm
    ax.hist(X.flatten(), bins=20, density=True, alpha=0.5)

    # GMM-Kurve
    ax.plot(x, density)

    ax.set_title(f"GMM (k={k})")

    return fig

def feature_hist(players, position_group, feature, bins=10, filter_zeros = False):
    pos_players = filter(players, position_group)
    if filter_zeros:
        values = pos_players[pos_players[feature] != 0][feature]
    else:
        values = pos_players[feature]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(values, bins=bins)

    ax.set_title(f"Verteilung von {feature} bei {position_group}")
    ax.set_xlabel(feature)
    ax.set_ylabel("Anzahl Spieler")

    return fig