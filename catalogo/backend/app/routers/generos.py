from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[schemas.GeneroOut])
def listar_generos(db: Session = Depends(get_db)):
    logger.info("Listando gêneros")
    return db.query(models.Genero).all()


@router.post("/", response_model=schemas.GeneroOut, status_code=201)
def criar_genero(payload: schemas.GeneroCreate, db: Session = Depends(get_db)):
    existente = db.query(models.Genero).filter(models.Genero.nome == payload.nome).first()
    if existente:
        raise HTTPException(status_code=400, detail="Gênero já existe")
    genero = models.Genero(**payload.model_dump())
    db.add(genero)
    db.commit()
    db.refresh(genero)
    logger.info(f"Gênero criado: {genero.nome}")
    return genero


@router.delete("/{genero_id}", status_code=204)
def deletar_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = db.query(models.Genero).filter(models.Genero.id == genero_id).first()
    if not genero:
        raise HTTPException(status_code=404, detail="Gênero não encontrado")
    logger.info(f"Gênero deletado: {genero.nome}")
    db.delete(genero)
    db.commit()
