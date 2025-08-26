from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:123456@localhost:5432/faculdades'
    JWT_SECRET: str = '3WtaxTJM6hDdbAHwUnAl8jHjWVEzb9rhji12dTQb2J4'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    

    """
    ALGORITHM: str = 'HS256'
    
    # 60 mins * 24 horas * 7 dias => 1 Semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


    class Config:
        case_sensitive = True

settings: Settings = Settings()