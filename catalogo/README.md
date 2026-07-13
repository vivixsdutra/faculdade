# 🎬 CineLog — Catálogo de Filmes & Séries

Aplicação fullstack para catalogar filmes e séries com avaliações de usuários.

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | FastAPI (Python 3.11) |
| Frontend | React 18 + Vite |
| Banco de dados | PostgreSQL 15 |
| Testes | Pytest |
| Orquestração | Docker + Docker Compose |

---

## 🚀 Como executar

### Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando
- [Git](https://git-scm.com/)

### 1. Clone o repositório

```bash
git clone <url-do-seu-repositorio>
cd catalogo
```

### 2. Suba todos os serviços com um único comando

```bash
docker compose up --build
```

> Na primeira execução, o Docker vai baixar as imagens e instalar as dependências.  
> Isso pode levar alguns minutos.

### 3. Acesse a aplicação

| Serviço | URL |
|---|---|
| Frontend | http://localhost:5173 |
| API (Swagger) | http://localhost:8000/docs |
| API (ReDoc) | http://localhost:8000/redoc |

### 4. Para parar

```bash
docker compose down
```

Para também remover os dados do banco:

```bash
docker compose down -v
```

---

## 🧪 Executando os testes

```bash
# Com os containers rodando:
docker compose exec backend pytest app/tests/ -v

# Ou direto na pasta backend (com Python instalado localmente):
cd backend
pip install -r requirements.txt pytest httpx
pytest app/tests/ -v
```

---

## 📁 Estrutura do projeto

```
catalogo/
├── backend/
│   ├── app/
│   │   ├── main.py          # Entrada da aplicação FastAPI
│   │   ├── database.py      # Configuração do SQLAlchemy
│   │   ├── models.py        # Modelos do banco (ORM)
│   │   ├── schemas.py       # Schemas Pydantic (validação)
│   │   ├── routers/
│   │   │   ├── filmes.py    # Rotas de filmes e avaliações
│   │   │   ├── generos.py   # Rotas de gêneros
│   │   │   └── avaliacoes.py
│   │   └── tests/
│   │       └── test_api.py  # Testes com pytest
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.jsx         # Tela 1: Catálogo com filtros
│   │   │   ├── DetalheFilme.jsx # Tela 2: Detalhe + avaliações
│   │   │   ├── FormFilme.jsx    # Tela 3: Cadastro/edição
│   │   │   └── Generos.jsx      # Tela 4: Gerenciar gêneros
│   │   ├── api.js               # Chamadas à API
│   │   ├── App.jsx
│   │   └── index.css
│   ├── vite.config.js
│   └── Dockerfile
├── postgres/
│   └── init.sql
└── docker-compose.yml
```

---

## 🗃️ Banco de Dados

### Diagrama de relacionamentos

```
filmes (1) ──── (N) avaliacoes      ← relação N para 1
filmes (N) ──── (M) generos         ← relação N para M (via filme_genero)
```

### Tabelas

**filmes**
```
id | titulo | tipo | ano | sinopse | diretor | poster_url | duracao_min
```

**generos**
```
id | nome
```

**filme_genero** (pivot N:M)
```
filme_id | genero_id
```

**avaliacoes**
```
id | filme_id | autor | nota | comentario
```

---

## 🔌 Rotas da API

### Filmes

| Método | Rota | Descrição |
|---|---|---|
| GET | `/filmes/` | Lista todos (filtros: `tipo`, `genero_id`) |
| GET | `/filmes/{id}` | Detalhe de um filme |
| POST | `/filmes/` | Cria novo filme |
| PUT | `/filmes/{id}` | Atualiza filme |
| DELETE | `/filmes/{id}` | Remove filme |
| GET | `/filmes/{id}/avaliacoes` | Lista avaliações do filme |
| POST | `/filmes/{id}/avaliacoes` | Cria avaliação |

### Gêneros

| Método | Rota | Descrição |
|---|---|---|
| GET | `/generos/` | Lista gêneros |
| POST | `/generos/` | Cria gênero |
| DELETE | `/generos/{id}` | Remove gênero |

### Avaliações

| Método | Rota | Descrição |
|---|---|---|
| PUT | `/avaliacoes/{id}` | Edita avaliação |
| DELETE | `/avaliacoes/{id}` | Remove avaliação |

---

## 📋 Boas práticas de uso

- **Crie os gêneros primeiro** antes de adicionar filmes, para poder associá-los.
- A **URL do poster** deve ser uma imagem acessível publicamente (ex: de IMDB, TMDB, etc.)
- As notas de avaliação devem estar entre **0.0 e 10.0**.
- Acesse o **Swagger em `/docs`** para testar todas as rotas diretamente no navegador.
- Logs do backend ficam visíveis com: `docker compose logs backend -f`

---

## 📊 Visualizando logs

```bash
# Todos os serviços
docker compose logs -f

# Só o backend
docker compose logs backend -f

# Só o banco
docker compose logs db -f
```

---

## 🔍 Acessando o banco diretamente

```bash
docker compose exec db psql -U postgres -d catalogo

# Alguns comandos úteis dentro do psql:
\dt          -- lista tabelas
\d filmes    -- estrutura da tabela filmes
SELECT * FROM filmes;
SELECT * FROM generos;
SELECT * FROM avaliacoes;
```
