# backend/app/main.py

from fastapi import FastAPI
from app.db.session import Base, engine
from app.db import models
from app.routers import responses, analysis
#from db.session import Base, engine
#from db import models
#from routers import responses, analysis

app = FastAPI(title="Polis-like Consensus API")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(responses.router, prefix="/api/responses")
app.include_router(analysis.router, prefix="/api/analysis")
