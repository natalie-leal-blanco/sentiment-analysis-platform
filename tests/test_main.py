import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json() == {"message": "Hello, Sentiment Analysis API is working!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@patch('app.main.sentiment_analyzer')
def test_analyze_sentiment(mock_analyzer):
    # Configure the mock
    mock_analyzer.return_value = [{"label": "POSITIVE", "score": 0.9}]
    
    # Test request
    response = client.post(
        "/analyze",
        json={"texts": ["This is a test message"]}
    )
    
    assert response.status_code == 200
    assert "results" in response.json()