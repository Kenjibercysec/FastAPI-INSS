from fastapi.testclient import TestClient
from .api import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={
        "tipo_dispositivo": "computador",
        "numero_tombamento": "123456",
        "marca": "lenovo",
        "memoria_ram": "16GB",
        "armazenamento": "1TB",
        "tipo_armazenamento": "SSD",
        "funcionando": "sim",
        "local_atual": "sala de manutencao",
        "descricao": "em perfeito estado",
        "data_analise": "2025-01-01"
    })
    assert response.status_code == 200
    assert response.json()["tipo_dispositivo"] == "computador"

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
