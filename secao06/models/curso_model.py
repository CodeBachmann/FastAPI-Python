# models/artigo_model.py
from __future__ import annotations
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models.usuario_model import UsuarioModel

class ArtigoModel(SQLModel, table=True):
    __tablename__ = "artigos"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    url_fonte: str

    usuario_id: int = Field(foreign_key="usuarios.id")
    usuario: Optional["UsuarioModel"] = Relationship(back_populates="artigos")
