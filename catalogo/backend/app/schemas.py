from pydantic import BaseModel, Field
from typing import Optional, List

# ── Gênero ──────────────────────────────────────────
class GeneroBase(BaseModel):
    nome: str

class GeneroCreate(GeneroBase):
    pass

class GeneroOut(GeneroBase):
    id: int
    class Config:
        from_attributes = True

# ── Avaliação ────────────────────────────────────────
class AvaliacaoBase(BaseModel):
    autor: str
    nota: float = Field(..., ge=0.0, le=10.0)
    comentario: Optional[str] = None

class AvaliacaoCreate(AvaliacaoBase):
    pass

class AvaliacaoUpdate(BaseModel):
    autor: Optional[str] = None
    nota: Optional[float] = Field(None, ge=0.0, le=10.0)
    comentario: Optional[str] = None

class AvaliacaoOut(AvaliacaoBase):
    id: int
    filme_id: int
    class Config:
        from_attributes = True

# ── Filme ────────────────────────────────────────────
class FilmeBase(BaseModel):
    titulo: str
    tipo: str = Field(..., pattern="^(filme|serie)$")
    ano: Optional[int] = None
    sinopse: Optional[str] = None
    diretor: Optional[str] = None
    poster_url: Optional[str] = None
    duracao_min: Optional[int] = None

class FilmeCreate(FilmeBase):
    genero_ids: List[int] = []

class FilmeUpdate(BaseModel):
    titulo: Optional[str] = None
    tipo: Optional[str] = Field(None, pattern="^(filme|serie)$")
    ano: Optional[int] = None
    sinopse: Optional[str] = None
    diretor: Optional[str] = None
    poster_url: Optional[str] = None
    duracao_min: Optional[int] = None
    genero_ids: Optional[List[int]] = None

class FilmeOut(FilmeBase):
    id: int
    generos: List[GeneroOut] = []
    avaliacoes: List[AvaliacaoOut] = []
    class Config:
        from_attributes = True

class FilmeList(FilmeBase):
    id: int
    generos: List[GeneroOut] = []
    class Config:
        from_attributes = True
