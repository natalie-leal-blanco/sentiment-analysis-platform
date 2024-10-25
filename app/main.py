from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.utils.config import get_settings
from transformers import pipeline
from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    texts: List[str]

app = FastAPI()
settings = get_settings()

# Initialize sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello, Sentiment Analysis API is working!"}

@app.get("/test")
async def test_endpoint():
    return {
        "status": "success",
        "message": "Test endpoint is working"
    }

@app.post("/analyze")
async def analyze_sentiment(request: TextRequest):
    try:
        results = sentiment_analyzer(request.texts)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))