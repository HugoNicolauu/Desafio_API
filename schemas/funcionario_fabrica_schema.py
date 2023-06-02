from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Funcionario_FabricaSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    rg: str
    cpf: str
    cep: str
    

    
    class config:
        orm_mode = True

class Funcionario_FabricaSchema(Funcionario_FabricaSchemaBase):
    data_adimissao : datetime
    data_hora_alteracao: datetime
    endereco:str
    bairro:str
    cidade:str