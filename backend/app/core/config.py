# backend/app/core/config.py

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./polis.db")

    class Config:
        env_file = ".env"


settings = Settings()
