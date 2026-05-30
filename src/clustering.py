import streamlit as st
import pandas as pd
import numpy as np

from src.statics import feature_sets

@st.cache_data(show_spinner="Forme Spielercluster ...")
def cluster(players):
    clusters = []
    for (features, positions) in feature_sets:
        players_in_group = players[players[positions].any(axis=1)]

        stats = players_in_group[features].apply(pd.to_numeric, errors="coerce")
        pcts = stats.rank(pct=True)
    
    return clusters

def kmeans(X, k, max_iters=100):

    centroids = initialize_centroids(X, k)

    for _ in range(max_iters):

        clusters = assign_clusters(X, centroids)

        new_centroids = update_centroids(X, clusters, k)

        # Abbruchbedingung
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return clusters, centroids

def k_value():
    return

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def initialize_centroids(X, k):
    indices = np.random.choice(len(X), k, replace = False)
    return X[indices]

def assign_clusters(X, centroids):

    clusters = []

    for point in X:

        distances = []

        for centroid in centroids:
            distance = euclidean_distance(point, centroid)
            distances.append(distance)

        cluster = np.argmin(distances)

        clusters.append(cluster)

    return np.array(clusters)

def update_centroids(X, clusters, k):

    centroids = []

    for cluster in range(k):

        cluster_points = X[clusters == cluster]

        centroid = np.mean(cluster_points, axis=0)

        centroids.append(centroid)

    return np.array(centroids)