# backend/app/polis/consensus.py

import pandas as pd
from typing import Dict


def compute_consensus(matrix: pd.DataFrame, clusters):
    df = matrix.copy()
    df["cluster"] = clusters
    consensus = {}

    for q in matrix.columns:
        if q == "cluster":
            continue
        rates = []
        for c in set(clusters):
            sub = df[df["cluster"] == c][q]
            if len(sub) == 0:
                continue
            agree_rate = (sub == 1).sum() / len(sub)
            rates.append(agree_rate)
        if rates:
            consensus[q] = min(rates)  # 全クラスタでの最低賛成率
    return consensus
