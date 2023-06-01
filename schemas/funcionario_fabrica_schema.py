from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Funcionario_FabricaSchema(BaseModel):
    id: Optional[int]
    nome: str
    rg: str
    cpf: str
    data_adimissao : datetime
    data_hora_alteracao: datetime
    cep: str
    endereco: str
    bairro: str
    cidade: str
    
    
    class config:
        orm_mode = True
    