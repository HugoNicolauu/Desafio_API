from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Funcionario_FabricaSchema(BaseModel):
    id: Optional[int]
    nome: str
    rg: str
    cpf: str
    data_adimissao : Optional[datetime]
    data_hora_alteracao: Optional[datetime]
    cep: str
    
    
    class config:
        orm_mode = True
    