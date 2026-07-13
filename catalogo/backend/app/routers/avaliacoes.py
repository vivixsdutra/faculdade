from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.put("/{avaliacao_id}", response_model=schemas.AvaliacaoOut)
def atualizar_avaliacao(avaliacao_id: int, payload: schemas.AvaliacaoUpdate, db: Session = Depends(get_db)):
    avaliacao = db.query(models.Avaliacao).filter(models.Avaliacao.id == avaliacao_id).first()
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(avaliacao, key, value)
    db.commit()
    db.refresh(avaliacao)
    logger.info(f"Avaliação atualizada: id={avaliacao_id}")
    return avaliacao


@router.delete("/{avaliacao_id}", status_code=204)
def deletar_avaliacao(avaliacao_id: int, db: Session = Depends(get_db)):
    avaliacao = db.query(models.Avaliacao).filter(models.Avaliacao.id == avaliacao_id).first()
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    logger.info(f"Avaliação deletada: id={avaliacao_id}")
    db.delete(avaliacao)
    db.commit()
