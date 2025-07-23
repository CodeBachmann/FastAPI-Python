from pydantic import BaseModel
from typing import Optional

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos_dic = [
    Curso(id=1, titulo="Como fazer fogo", aulas=4, horas=18),
    Curso(id=2, titulo="Arvores", aulas=5, horas=12)
]