from typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from sqlmodel import SQLModel, select
from core.auth import oauth2_schema
from core.configs import settings
from models.usuario_model import UsuarioModel
from sqlalchemy.ext.asyncio import AsyncSession


class TokenData(SQLModel):
    username: Optional[str] = None

async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()

async def get_current_user(db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel:
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial',
        headers={"WWW-Authenticate": "Bearer"},

    )
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET, 
            algorithms=[settings.ALGORITHM], 
            options={"verify_aud"}
        )
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        
        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credential_exception
    
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == int(token_data.username))
        result = session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if usuario is None:
            raise credential_exception
        
        return usuario
    
