# backend/app/routers/responses.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.db import models
from app.schemas.survey import ResponseBatchIn, ResponseIn


router = APIRouter(prefix="/responses", tags=["responses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", status_code=201)
def add_responses(payload: ResponseBatchIn, db: Session = Depends(get_db)):
    for r in payload.responses:
        db_obj = models.Response(
            user_id=r.user_id,
            question_id=r.question_id,
            answer=r.answer,
        )
        db.add(db_obj)
    db.commit()
    return {"status": "ok", "count": len(payload.responses)}
