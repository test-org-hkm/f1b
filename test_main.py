from fastapi.testclient import TestClient
from main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Birthday Calculator API"}

def test_calculate_age_valid():
    # Test with a date 25 years ago
    test_date = (datetime.now() - timedelta(days=365*25)).strftime("%Y-%m-%d")
    response = client.post("/calculate-age", json={"birth_date": test_date})
    assert response.status_code == 200
    assert response.json()["age"] == 25

def test_calculate_age_invalid_format():
    response = client.post("/calculate-age", json={"birth_date": "invalid-date"})
    assert response.status_code == 200
    assert "error" in response.json()
    assert "Invalid date format" in response.json()["error"] 