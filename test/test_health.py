from fastapi.testclient import TestClient

from agente_atendimento.main import app

client = TestClient(app)

def test_health_retorna_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status" : "ok"}