from pydantic import BaseModel
from typing import List, Dict


class SentimentRequest(BaseModel):
    texts: List[str]


class SentimentResponse(BaseModel):
    sentiments: List[Dict[str, float]]
    processing_time: float
