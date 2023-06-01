from pydantic import  BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://dev:1234@localhost:3306/bdo1'
    DB_URL2: str = 'mysql+asyncmy://dev:1234@localhost:3306/bdo2'
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
        

settings: Settings = Settings()