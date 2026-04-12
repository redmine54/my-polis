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

    from app.schemas.survey import ResponseIn

    responses = [
        ResponseIn(
            user_id=r.user_id,
            question_id=r.question_id,
            answer=r.answer,
        )
        for r in rows
    ]

    matrix, users, questions = responses_to_matrix(responses)
    clusters = cluster_users(matrix)
    consensus = compute_consensus(matrix, clusters)

    cluster_out: List[ClusterResultOut] = [
        ClusterResultOut(user_id=u, cluster_id=int(c))
        for u, c in zip(users, clusters)
    ]
    consensus_out: List[ConsensusOut] = [
        ConsensusOut(question_id=q, agreement_rate=float(a))
        for q, a in consensus.items()
    ]

    return {
        "clusters": cluster_out,
        "consensus": consensus_out,
    }
