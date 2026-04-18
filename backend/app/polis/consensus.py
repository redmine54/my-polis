# backend/app/polis/consensus.py

import pandas as pd
from typing import Dict


def compute_consensus(matrix: pd.DataFrame, clusters):
    df = matrix.copy()
    df["cluster"] = clusters

    print(f"clusters: {set(clusters)}")        # クラスタ一覧
    print(f"matrix dtypes:\n{matrix.dtypes}")  # 型確認
    print(f"matrix sample:\n{matrix.head()}")  # 実データ確認

    consensus = {}
    print(f"compute_consensus(): ¥n{df}")
    for q in matrix.columns:
        if q == "cluster":
            continue
        rates = []
        for c in set(clusters):
            sub = df[df["cluster"] == c][q]

            sub = df[df["cluster"] == c][q]
            sub_valid = sub.dropna()            # NaNを除外

            #print(f"q={q}, cluster={c}, values={sub_valid.tolist()}")  # 追加

            #if len(sub) == 0:
            #    continue
            # クラスタごとの賛成率を計算
            # NaNも len(sub) に含まれるため賛成率が低く見える
            # agree_rate = (sub == 1).sum() / len(sub)
            """
            # 現状：NaNも len(sub) に含まれるため賛成率が低く見える
            # 改善案：NaNを除外してから計算
            """
            if len(sub_valid) == 0:
                continue
            sub_valid = sub.dropna()
            agree_rate = (sub_valid == 1).sum() / len(sub_valid)
            #print(f"consensus.py:  agree_rate={agree_rate}") # 追加
            rates.append(agree_rate)

        if rates:
            # 最低賛成率を合意スコアとして記録
            consensus[q] = min(rates)
            """
            min() を使うことで、「一部のクラスタだけが賛成している意見」ではなく、対立するグループ全員が賛成できる意見を高スコアにできます。これがPol.isにおける「合意」の本質です。
            意見A: rates=[1.0, 0.9, 0.8] → min=0.8  ✅ 全員が支持
            意見B: rates=[1.0, 0.0, 1.0] → min=0.0  ❌ クラスタ1が反対

            戻り値：スコアが高い意見ほど全グループで合意されている意見です。
                {
                    "s1": 0.0,   # クラスタ1が反対 → 合意できていない
                    "s2": 0.8,   # 全クラスタで高い賛成率 → 合意できている
                    "s3": 0.6,
                }

            """
    return consensus
