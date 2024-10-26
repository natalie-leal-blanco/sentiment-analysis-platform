from fastapi import APIRouter, HTTPException
from app.models.schemas import SentimentRequest, SentimentResponse
from app.models.sentiment import SentimentAnalyzer
from datetime import datetime
import logging

router = APIRouter()
analyzer = SentimentAnalyzer()
logger = logging.getLogger(__name__)


@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest) -> SentimentResponse:
    start_time = datetime.now()

    try:
        sentiments = analyzer.predict(request.texts)
        processing_time = (datetime.now() - start_time).total_seconds()

        return SentimentResponse(sentiments=sentiments, processing_time=processing_time)

    except Exception as e:
        logger.error(f"API error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
