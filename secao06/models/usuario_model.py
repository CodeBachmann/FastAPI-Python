# models/usuario_model.py
from __future__ import annotations
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from models.artigo_model import ArtigoModel

class UsuarioModel(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str

    artigos: List["ArtigoModel"] = Relationship(back_populates="usuario")
