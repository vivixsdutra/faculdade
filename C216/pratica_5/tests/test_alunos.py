from fastapi.testclient import TestClient
from app.main import app
from app.database import alunos, contadores_matricula

client = TestClient(app)


def limpar_dados():
    alunos.clear()
    contadores_matricula["GES"] = 0
    contadores_matricula["GEC"] = 0


def test_adicionar_3_alunos_por_curso():
    limpar_dados()

    alunos_teste = [
        {"nome": "Ana", "email": "ana@email.com", "curso": "GES"},
        {"nome": "Bruno", "email": "bruno@email.com", "curso": "GES"},
        {"nome": "Carla", "email": "carla@email.com", "curso": "GES"},
        {"nome": "Diego", "email": "diego@email.com", "curso": "GEC"},
        {"nome": "Eva", "email": "eva@email.com", "curso": "GEC"},
        {"nome": "Felipe", "email": "felipe@email.com", "curso": "GEC"},
    ]

    for aluno in alunos_teste:
        response = client.post("/api/v1/alunos/", json=aluno)
        assert response.status_code == 200

    assert len(alunos) == 6
    assert "GES1" in alunos
    assert "GES2" in alunos
    assert "GES3" in alunos
    assert "GEC1" in alunos
    assert "GEC2" in alunos
    assert "GEC3" in alunos


def test_listar_alunos():
    limpar_dados()

    client.post("/api/v1/alunos/", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "curso": "GES"
    })

    response = client.get("/api/v1/alunos/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_buscar_aluno_por_id():
    limpar_dados()

    client.post("/api/v1/alunos/", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "curso": "GES"
    })

    response = client.get("/api/v1/alunos/GES1")

    assert response.status_code == 200
    assert response.json()["id"] == "GES1"
    assert response.json()["nome"] == "Ana"


def test_atualizar_aluno():
    limpar_dados()

    client.post("/api/v1/alunos/", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "curso": "GES"
    })

    response = client.patch("/api/v1/alunos/GES1", json={
        "nome": "Ana Atualizada"
    })

    assert response.status_code == 200
    assert response.json()["nome"] == "Ana Atualizada"


def test_remover_aluno():
    limpar_dados()

    client.post("/api/v1/alunos/", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "curso": "GES"
    })

    response = client.delete("/api/v1/alunos/GES1")

    assert response.status_code == 200
    assert "GES1" not in alunos


def test_id_nao_deve_ser_reutilizado_apos_delete():
    limpar_dados()

    client.post("/api/v1/alunos/", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "curso": "GES"
    })

    client.delete("/api/v1/alunos/GES1")

    response = client.post("/api/v1/alunos/", json={
        "nome": "Bruno",
        "email": "bruno@email.com",
        "curso": "GES"
    })

    assert response.status_code == 200
    assert response.json()["id"] == "GES2"