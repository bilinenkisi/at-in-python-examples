from fastapi.testclient import TestClient
from src.app import app
import pytest

client = TestClient(app)

def test_read_data():
    response = client.get("/data")
    # assert response.status_code == 200
    # assert response.json() == {"items": ["a", "b", "c"]}

def test_read_error():
    with pytest.raises(Exception):
        response = client.get("/data/error")
