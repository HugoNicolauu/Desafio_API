from sqlalchemy import  Column, Integer, String,DateTime,Date
from datetime import datetime

from core.configs import Settings

class Funcionario_fabricaModel(Settings.DBBaseModel):
    __tablename__ = 'funcionarios_fabrica'
    
    id: int = Column(Integer,primary_key=True,autoincrement=True)
    nome: str = Column(String(100))
    rg: str = Column(String(20),unique=True)
    cpf: str = Column(String(14),unique=True)
    data_adimissao:datetime = Column(Date)
    data_hora_alteracao: datetime = Column(DateTime)
    cep: str = Column(String(10))
    endereco: str = Column(String(50))
    bairro: str = Column(String(50))
    cidade: str = Column(String(50))