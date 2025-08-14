from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import HTTPException, status

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    # @field_validator("titulo")
    # def validar_titulo(cls, value):
    #     palavras = value.split(" ")
    #     if len(palavras) < 3:
    #         raise ValueError("O Titulo deve conter ao menos 3 palavras")
    #     return value

cursos_dic = [  
    Curso(id=1, titulo="Como fazer fogo", aulas=4, horas=18),
    Curso(id=2, titulo="Arvores", aulas=5, horas=12)
]