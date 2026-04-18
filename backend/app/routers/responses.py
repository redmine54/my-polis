# backend/app/routers/responses.py

from fastapi import APIRouter, Depends
from fastapi import UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import csv
import io

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

# 一括登録エンドポイント(JSON)
@router.post("/", status_code=201)
def add_responses(payload: ResponseBatchIn, db: Session = Depends(get_db)):
    """
    JSONファイルをアップロードして responses テーブルに登録する
    """
    for r in payload.responses:
        db_obj = models.Response(
            user_id=r.user_id,
            question_id=r.question_id,
            answer=r.answer,
        )
        db.add(db_obj)
    db.commit()
    return {"status": "ok", "count": len(payload.responses)}

#@router.post("/upload-csv", status_code=201)
#def add_responses_csv(filepath: str, db: Session = Depends(get_db)):
#    # ここにCSVファイルの処理ロジックを実装
#    pass



# 一括登録エンドポイント(CSV)
@router.post("/upload-csv", status_code=201)
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    CSVファイルをアップロードして responses テーブルに登録する
    """
    # CSV以外のファイルを拒否
    if not file.filename.endswith(".csv"):
        return {"status": "error", "message": "CSVファイルのみ対応しています"}

    # ファイルを読み込む
    content = await file.read()
    text = content.decode("utf-8-sig")  # BOM付きUTF-8にも対応

    # 既存データをクリア（再インポート時の重複防止）
    db.query(models.Response).delete()
    db.commit()

    # CSVをパース（ヘッダーとして自動的に読み込む）
    reader = csv.DictReader(io.StringIO(text))

    count = 0
    for row in reader:
        # 2行目を最初のデータ行として読み込み開始
        #print(f"user_id={row['user_id']} question_id={row['question_id']}")

        obj = models.Response(
            user_id=row["user_id"],
            question_id=row["question_id"],
            answer=int(row["answer"]),  # +1 / -1 / 0
        )
        db.add(obj)
        count += 1

    db.commit()
    print(f"status=ok, count={count}")
    return {"status": "ok", "count": count}
