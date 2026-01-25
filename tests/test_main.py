from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_create_item():
    item_payload = {"id": 1, "name": "Laptop", "price": 1500.0, "is_offer": False}
    response = client.post("/items", json=item_payload)
    assert response.status_code == 201
    assert response.json() == item_payload

def test_get_items():
    # წინასწარ ვამატებთ, რომ სია ცარიელი არ იყოს
    client.post("/items", json={"id": 2, "name": "Mouse", "price": 20.0})
    
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0