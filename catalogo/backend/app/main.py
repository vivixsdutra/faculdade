from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import filmes, generos, avaliacoes
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catálogo de Filmes/Séries", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(filmes.router, prefix="/filmes", tags=["Filmes"])
app.include_router(generos.router, prefix="/generos", tags=["Gêneros"])
app.include_router(avaliacoes.router, prefix="/avaliacoes", tags=["Avaliações"])

@app.get("/")
def root():
    logger.info("Health check chamado")
    return {"status": "ok", "message": "Catálogo de Filmes API"}
