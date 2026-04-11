# backend/app/db/models.py

from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    question_id = Column(String, index=True)
    answer = Column(Integer)  # +1 / -1 / 0


class ClusterResult(Base):
    __tablename__ = "cluster_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    cluster_id = Column(Integer, index=True)


class ConsensusStatement(Base):
    __tablename__ = "consensus_statements"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(String, index=True)
    agreement_rate = Column(Float)
