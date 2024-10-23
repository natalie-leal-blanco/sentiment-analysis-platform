from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
from app.utils.config import get_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Sentiment Analysis API")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Sentiment Analysis API")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.api_port)
