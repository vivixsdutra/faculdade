from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Tabela pivot N:M — Filme <-> Genero
filme_genero = Table(
    "filme_genero",
    Base.metadata,
    Column("filme_id", Integer, ForeignKey("filmes.id", ondelete="CASCADE"), primary_key=True),
    Column("genero_id", Integer, ForeignKey("generos.id", ondelete="CASCADE"), primary_key=True),
)

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    tipo = Column(String(50), nullable=False)  # "filme" ou "serie"
    ano = Column(Integer)
    sinopse = Column(Text)
    diretor = Column(String(150))
    poster_url = Column(String(500))
    duracao_min = Column(Integer)

    # N:M
    generos = relationship("Genero", secondary=filme_genero, back_populates="filmes")
    # N:1 (um filme tem muitas avaliações)
    avaliacoes = relationship("Avaliacao", back_populates="filme", cascade="all, delete")


class Genero(Base):
    __tablename__ = "generos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False)

    filmes = relationship("Filme", secondary=filme_genero, back_populates="generos")


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    filme_id = Column(Integer, ForeignKey("filmes.id", ondelete="CASCADE"), nullable=False)
    autor = Column(String(100), nullable=False)
    nota = Column(Float, nullable=False)  # 0.0 a 10.0
    comentario = Column(Text)

    # N:1
    filme = relationship("Filme", back_populates="avaliacoes")
