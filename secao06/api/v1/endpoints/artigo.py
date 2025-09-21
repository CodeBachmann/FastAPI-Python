from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from models.artigo_model import ArtigoModel
from core.deps import get_session
from sqlmodel import select

# Bypass Warning  SQLModel Select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED, response_model=ArtigoModel)
async def post_curso(curso: ArtigoModel, db: AsyncSession = Depends(get_session)):
    novo_curso = ArtigoModel(titulo = curso.titulo, horas = curso.horas, aulas = curso.aulas)

    db.add(novo_curso)
    await db.commit()
    return novo_curso


@router.get('/', response_model=List[ArtigoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)) -> List[ArtigoModel]:
        query = select(ArtigoModel)
        result = await db.execute(query)
        cursos: List[ArtigoModel] = result.scalars().all()

        return cursos

@router.get('/{curso_id}', response_model=ArtigoModel)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == curso_id)
        result = await session.execute(query)
        curso: ArtigoModel = result.scalar_one_or_none()

    if curso:
        return curso
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
@router.put('/{curso_id}', response_model=ArtigoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: ArtigoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == curso_id)
        result = await session.execute(query)
        curso_up: ArtigoModel = result.scalar_one_or_none()

        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.horas = curso.horas
            curso_up.aulas = curso.aulas

            await session.commit()
            return curso_up
        else:
            raise HTTPException(detail="ID Não Encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: ArtigoModel = result.scalar_one_or_none()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="ID Não Encontrado", status_code=status.HTTP_404_NOT_FOUND)