from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class FuncionarioSchema(BaseModel):
    id: Optional[int]
    nome: str
    rg: str
    cpf: str
    data_admissao : date
    data_hora_alteracao: datetime
    cep: str
    
    class Config:
        orm_mode = True
    
    