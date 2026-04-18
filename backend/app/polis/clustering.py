# backend/app/polis/clustering.py

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import SpectralClustering
import numpy as np
import pandas as pd

def cluster_users(matrix: pd.DataFrame, n_clusters: int = 3):
    """
    ユーザーをクラスター分けする
    """
    if matrix.shape[0] < n_clusters:
        n_clusters = max(1, matrix.shape[0])

    # コサイン類似度の計算
    sim = cosine_similarity(matrix.values)

    """
    affinity='precomputed' は 0〜1の対称行列 を期待しています。
    コサイン類似度は -1〜1 を返すため、負の値が含まれるとエラーになることがあります。
    """
    # 負の値を除去（-1〜1 → 0〜1 に正規化
    sim = np.clip(sim, 0, 1)

    # スペクトラルクラスタリング
    clustering = SpectralClustering(
        n_clusters=n_clusters,
        affinity="precomputed",  # 類似度行列を直接渡す
        assign_labels="kmeans",  # 最終的なラベル割り当てにk-meansを使用
        random_state=42,         # 再現性のための固定シード
    )
    """
    #     ユーザーごとのクラスタ番号（0始まり）
    # # 例: labels = array([0, 1, 0, 2, 1, 0])
    """
    labels = clustering.fit_predict(sim)
    return labels
