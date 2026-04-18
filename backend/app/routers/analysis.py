# backend/app/routers/analysis.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.db import models
from app.schemas.survey import ClusterResultOut, ConsensusOut
from app.polis.preprocessing import responses_to_matrix
from app.polis.clustering import cluster_users
from app.polis.consensus import compute_consensus

router = APIRouter(prefix="/analysis", tags=["analysis"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/run")
def run_analysis(db: Session = Depends(get_db)):
    rows = db.query(models.Response).all()
    if not rows:
        return {"clusters": [], "consensus": []}
    print(f"run_analysis():DBから {len(rows)} 件のレスポンスを取得")
    from app.schemas.survey import ResponseIn

    responses = [
        ResponseIn(
            user_id=r.user_id,
            question_id=r.question_id,
            answer=r.answer,
        )
        for r in rows
    ]
    for i, r in enumerate(rows):
        pass
        #print(f"i={i}:  user_id={r.user_id}, question_id={r.question_id}, answer={r.answer}")

    # 生の投票レスポンスデータ（DBのレコード等）を、クラスタリングで使える数値行列に変換
    matrix, users, questions = responses_to_matrix(responses)
    #print(f"run_analysis(): matrix={matrix}, users={users}")
    # ユーザーをクラスター分け
    clusters = cluster_users(matrix)
    #print(f"run_analysis(): clusters={clusters}")

    # クラスタ間の合意意見を抽出
    consensus = compute_consensus(matrix, clusters)
    #print(f"run_analysis(): consensus={consensus}")

    #print(f"run_analysis(): クラスタリングとコンセンサス計算完了")
    cluster_out: List[ClusterResultOut] = [
        ClusterResultOut(user_id=u, cluster_id=int(c))
        for u, c in zip(users, clusters)
    ]
    #print(f"run_analysis(): クラスタリング結果 {len(cluster_out)} 件" )
    consensus_out: List[ConsensusOut] = [
        ConsensusOut(question_id=q, agreement_rate=float(a))
        for q, a in consensus.items()
    ]
    print(f"run_analysis(): クラスタリング結果 {len(cluster_out)} 件, コンセンサス結果 {len(consensus_out)} 件" )
    return {
        "clusters": cluster_out,
        "consensus": consensus_out,
    }
