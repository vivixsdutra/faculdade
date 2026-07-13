from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app import models, schemas
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[schemas.FilmeList])
def listar_filmes(
    tipo: Optional[str] = Query(None),
    genero_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    logger.info(f"Listando filmes | tipo={tipo} genero_id={genero_id}")
    query = db.query(models.Filme)
    if tipo:
        query = query.filter(models.Filme.tipo == tipo)
    if genero_id:
        query = query.filter(models.Filme.generos.any(models.Genero.id == genero_id))
    return query.all()


@router.get("/{filme_id}", response_model=schemas.FilmeOut)
def obter_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    logger.info(f"Filme obtido: {filme.titulo}")
    return filme


@router.post("/", response_model=schemas.FilmeOut, status_code=201)
def criar_filme(payload: schemas.FilmeCreate, db: Session = Depends(get_db)):
    generos = db.query(models.Genero).filter(models.Genero.id.in_(payload.genero_ids)).all()
    filme = models.Filme(**payload.model_dump(exclude={"genero_ids"}))
    filme.generos = generos
    db.add(filme)
    db.commit()
    db.refresh(filme)
    logger.info(f"Filme criado: {filme.titulo} (id={filme.id})")
    return filme


@router.put("/{filme_id}", response_model=schemas.FilmeOut)
def atualizar_filme(filme_id: int, payload: schemas.FilmeUpdate, db: Session = Depends(get_db)):
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    data = payload.model_dump(exclude_unset=True)
    if "genero_ids" in data:
        generos = db.query(models.Genero).filter(models.Genero.id.in_(data.pop("genero_ids"))).all()
        filme.generos = generos
    for key, value in data.items():
        setattr(filme, key, value)
    db.commit()
    db.refresh(filme)
    logger.info(f"Filme atualizado: {filme.titulo} (id={filme.id})")
    return filme


@router.delete("/{filme_id}", status_code=204)
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    logger.info(f"Filme deletado: {filme.titulo} (id={filme.id})")
    db.delete(filme)
    db.commit()


@router.get("/{filme_id}/avaliacoes", response_model=List[schemas.AvaliacaoOut])
def listar_avaliacoes(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme.avaliacoes


@router.post("/{filme_id}/avaliacoes", response_model=schemas.AvaliacaoOut, status_code=201)
def criar_avaliacao(filme_id: int, payload: schemas.AvaliacaoCreate, db: Session = Depends(get_db)):
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    avaliacao = models.Avaliacao(**payload.model_dump(), filme_id=filme_id)
    db.add(avaliacao)
    db.commit()
    db.refresh(avaliacao)
    logger.info(f"Avaliação criada para filme_id={filme_id} por {avaliacao.autor}")
    return avaliacao
