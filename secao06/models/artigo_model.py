from typing import Optional

from sqlmodel import Field, SQLModel, Relationship
from models.usuario_model import UsuarioModel

class ArtigoModel(SQLModel, table=True):
    __tablename__: str = "artigos"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    url_fonte: str
    usuario_id: int = Field(foreign_key="usuarios.id")
    usuarios: Optional["UsuarioModel"] = Relationship(back_populates="artigos", lazy="joined")