from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_add_invalid_input():
    response = client.get("/add", params={"a": "xyz", "b": 3})
    assert response.status_code == 422


def test_divide():
    response = client.get("/divide", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 2.5


def test_divide_by_zero():
    response = client.get("/divide", params={"a": 10, "b": 0})
    assert response.status_code == 400