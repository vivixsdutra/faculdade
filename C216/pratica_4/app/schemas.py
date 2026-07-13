from pydantic import BaseModel, EmailStr
from typing import Optional


class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    curso: str


class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    curso: Optional[str] = None


class AlunoResponse(BaseModel):
    id: str
    nome: str
    email: str
    curso: str
    matricula: int