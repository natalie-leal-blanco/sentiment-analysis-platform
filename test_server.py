from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, Sentiment Analysis API is working!"}


@app.get("/test")
async def test_endpoint():
    return {"status": "success", "message": "Test endpoint is working"}
