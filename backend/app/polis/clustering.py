# backend/app/polis/clustering.py

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import SpectralClustering
import numpy as np
import pandas as pd


def cluster_users(matrix: pd.DataFrame, n_clusters: int = 3):
    if matrix.shape[0] < n_clusters:
        n_clusters = max(1, matrix.shape[0])

    sim = cosine_similarity(matrix.values)
    clustering = SpectralClustering(
        n_clusters=n_clusters,
        affinity="precomputed",
        assign_labels="kmeans",
        random_state=42,
    )
    labels = clustering.fit_predict(sim)
    return labels
