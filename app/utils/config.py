from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Sentiment Analysis API"
    debug: bool = False
    model_path: str = "distilbert-base-uncased"
    api_port: int = 8000

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
