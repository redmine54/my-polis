# backend/app/schemas/survey.py

from pydantic import BaseModel
from typing import List


class ResponseIn(BaseModel):
    user_id: str
    question_id: str
    answer: int  # +1 / -1 / 0


class ResponseBatchIn(BaseModel):
    responses: List[ResponseIn]


class ClusterResultOut(BaseModel):
    user_id: str
    cluster_id: int


class ConsensusOut(BaseModel):
    question_id: str
    agreement_rate: float
