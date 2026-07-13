import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Banco em memória só para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def limpar_banco():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


# ── Gêneros ──────────────────────────────────────────
def test_criar_genero():
    r = client.post("/generos/", json={"nome": "Ação"})
    assert r.status_code == 201
    assert r.json()["nome"] == "Ação"

def test_listar_generos():
    client.post("/generos/", json={"nome": "Drama"})
    r = client.get("/generos/")
    assert r.status_code == 200
    assert len(r.json()) == 1

def test_criar_genero_duplicado():
    client.post("/generos/", json={"nome": "Comédia"})
    r = client.post("/generos/", json={"nome": "Comédia"})
    assert r.status_code == 400

def test_deletar_genero():
    r = client.post("/generos/", json={"nome": "Terror"})
    genero_id = r.json()["id"]
    r = client.delete(f"/generos/{genero_id}")
    assert r.status_code == 204


# ── Filmes ────────────────────────────────────────────
def _criar_filme(titulo="Inception", tipo="filme"):
    return client.post("/filmes/", json={
        "titulo": titulo,
        "tipo": tipo,
        "ano": 2010,
        "sinopse": "Sonhos dentro de sonhos.",
        "diretor": "Christopher Nolan",
        "genero_ids": [],
    })

def test_criar_filme():
    r = _criar_filme()
    assert r.status_code == 201
    assert r.json()["titulo"] == "Inception"

def test_listar_filmes():
    _criar_filme("Filme 1")
    _criar_filme("Filme 2")
    r = client.get("/filmes/")
    assert r.status_code == 200
    assert len(r.json()) == 2

def test_obter_filme():
    filme_id = _criar_filme().json()["id"]
    r = client.get(f"/filmes/{filme_id}")
    assert r.status_code == 200

def test_obter_filme_inexistente():
    r = client.get("/filmes/9999")
    assert r.status_code == 404

def test_atualizar_filme():
    filme_id = _criar_filme().json()["id"]
    r = client.put(f"/filmes/{filme_id}", json={"titulo": "Inception 2"})
    assert r.status_code == 200
    assert r.json()["titulo"] == "Inception 2"

def test_deletar_filme():
    filme_id = _criar_filme().json()["id"]
    r = client.delete(f"/filmes/{filme_id}")
    assert r.status_code == 204
    assert client.get(f"/filmes/{filme_id}").status_code == 404


# ── Avaliações ────────────────────────────────────────
def _criar_avaliacao(filme_id, nota=8.5):
    return client.post(f"/filmes/{filme_id}/avaliacoes", json={
        "autor": "João",
        "nota": nota,
        "comentario": "Ótimo filme!",
    })

def test_criar_avaliacao():
    filme_id = _criar_filme().json()["id"]
    r = _criar_avaliacao(filme_id)
    assert r.status_code == 201
    assert r.json()["nota"] == 8.5

def test_listar_avaliacoes():
    filme_id = _criar_filme().json()["id"]
    _criar_avaliacao(filme_id)
    _criar_avaliacao(filme_id, nota=7.0)
    r = client.get(f"/filmes/{filme_id}/avaliacoes")
    assert r.status_code == 200
    assert len(r.json()) == 2

def test_atualizar_avaliacao():
    filme_id = _criar_filme().json()["id"]
    av_id = _criar_avaliacao(filme_id).json()["id"]
    r = client.put(f"/avaliacoes/{av_id}", json={"nota": 9.0})
    assert r.status_code == 200
    assert r.json()["nota"] == 9.0

def test_deletar_avaliacao():
    filme_id = _criar_filme().json()["id"]
    av_id = _criar_avaliacao(filme_id).json()["id"]
    r = client.delete(f"/avaliacoes/{av_id}")
    assert r.status_code == 204

def test_nota_invalida():
    filme_id = _criar_filme().json()["id"]
    r = client.post(f"/filmes/{filme_id}/avaliacoes", json={
        "autor": "Maria", "nota": 15.0
    })
    assert r.status_code == 422
