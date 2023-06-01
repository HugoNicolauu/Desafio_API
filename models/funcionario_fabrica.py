from sqlalchemy import  Column, Integer, String, Date


from core.configs import Settings

class Funcionario_fabricaModel(Settings.DBBaseModel):
    __tablename__ = 'funcionarios_fabrica'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(100))
    rg = Column(String(20),unique=True)
    cpf = Column(String(14),unique=True)
    data_adimissao = Column(Date)
    data_hora_alteracao = Column(Date)
    cep = Column(String(10))
    endereco = Column(String(50))
    bairro = Column(String(50))
    cidade = Column(String(50))