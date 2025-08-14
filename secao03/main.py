from fastapi import FastAPI, status, HTTPException, Path, Query, Header, Depends
from fastapi.responses import Response
from models import Curso, cursos_dic
from typing import List, Optional, Any, Dict
from time import sleep

app = FastAPI(
    title="API de estudos do CodeBach", version="0.01", description="Uma API para estudar o framework FastAPI")

def fake_db():
    try:
        print('Conectando ao banco de dados...')
        sleep(1)
    finally:
        print("Fechando conexão com o banco de dados...")
        sleep(1)

@app.get('/')
async def raiz():
    return "Olá Mundo!"

@app.get('/cursos', description="Retorna todos os cursos", summary="Retorna todos os cursos", response_model=List[Curso], response_description="Cursos encontrados com Sucesso!!")
async def get_cursos(titulo: Optional[str] = None, db: Any = Depends(fake_db)):
    filtered_cursos_dic = []
    if titulo:
        print(titulo)
        for curso in cursos_dic:
            if titulo.lower() in curso.titulo.lower():
                filtered_cursos_dic.append(curso)
        if len(filtered_cursos_dic) == 0:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        return filtered_cursos_dic
    return cursos_dic

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title="ID do Curso", description="Deve ser entre 1 e 2", gt=0, lt=3), db: Any = Depends(fake_db)):
        for curso in cursos_dic:
            if curso.id == curso_id:
                return curso    

            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse ID não está registrado")
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    del curso.id
    curso_id = max(cursos_dic) + 1
    cursos_dic[curso_id] = curso
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos_dic:
        cursos_dic[curso_id] = curso.model_dump(exclude={"id"})  # Salva sem o campo "id"
        return cursos_dic[curso_id]  # Retorna limpo, sem "id"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esse ID não está registrado"
        )

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos_dic:
        del cursos_dic[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esse ID não está registrado"
        )

@app.get("/calculadora")
async def calcular(a:int = Query(gt=5), b:int = Query(gt=6), x_geek:str = Header() , c:int = Query(gt=7)):
    resultado = a + b + c
    print(f"X-GEEK: {x_geek}")
    return resultado


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)