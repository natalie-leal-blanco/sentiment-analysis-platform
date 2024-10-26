from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextRequest(BaseModel):
    texts: List[str]

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lazy load sentiment analyzer
sentiment_analyzer = None

def get_analyzer():
    global sentiment_analyzer
    if sentiment_analyzer is None:
        from transformers import pipeline
        sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer

@app.get("/")
async def read_root():
    return {"message": "Hello, Sentiment Analysis API is working!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze")
async def analyze_sentiment(request: TextRequest):
    try:
        analyzer = get_analyzer()
        results = analyzer(request.texts)
        return {"results": results}
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))