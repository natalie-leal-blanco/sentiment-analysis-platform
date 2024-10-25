from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_analyze_sentiment():
    response = client.post(
        "/analyze",
        json={"texts": ["This is a test"]}
    )
    assert response.status_code == 200
    assert "results" in response.json()