from fastapi import APIRouter

router =  APIRouter()

@router.get('/api/v1/cursos')
async def get_cursos():
    return {"msg": "todos os cursos"}