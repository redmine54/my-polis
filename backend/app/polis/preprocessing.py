# backend/app/polis/preprocessing.py

import pandas as pd
from typing import List
from app.schemas.survey import ResponseIn


def responses_to_matrix(responses: List[ResponseIn]):
    df = pd.DataFrame([r.dict() for r in responses])
    # user × question の行列
    matrix = df.pivot_table(
        index="user_id",
        columns="question_id",
        values="answer",
        fill_value=0,
    )
    return matrix, matrix.index.tolist(), matrix.columns.tolist()
