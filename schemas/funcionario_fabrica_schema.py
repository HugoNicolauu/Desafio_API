from typing import Optional
from pydantic import BaseModel
from datetime import datetime,date

class Funcionario_FabricaSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    rg: str
    cpf: str
    cep: str
    
    class Config: #Lembrete, SQLAlchemy does not return a dictionary, which is what pydantic expects by default. You can configure your model to also support loading from standard orm parameters
        orm_mode = True
    


class Funcionario_FabricaSchema(Funcionario_FabricaSchemaBase):
    data_admissao : date
    data_hora_alteracao: datetime
    endereco:str
    bairro:str
    cidade:str

class Funcionario_FabricaSchemaUp(Funcionario_FabricaSchemaBase):
    nome: Optional[str]
    rg: Optional[str]
    cpf: Optional[str]
    cep: Optional[str]
    