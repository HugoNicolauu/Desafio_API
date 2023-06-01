from typing import List
from datetime import datetime

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.funcionario_fabrica import Funcionario_fabricaModel
from models.funcionario import FuncionarioModel
from schemas.funcionario_fabrica_schema import Funcionario_FabricaSchema
from core.deps import get_session, get_session2
from utils.cep_busca import busca_cep

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED,response_class=Funcionario_FabricaSchema)
async def post_funcionario_fabrica(func_fab:Funcionario_FabricaSchema,db: AsyncSession = Depends(get_session2)):
    result= busca_cep(func_fab.cep)
    novo_func_fab = Funcionario_fabricaModel(nome=func_fab.nome,rg=func_fab.rg,
                                             cpf=func_fab.cpf,cep=func_fab.cep,
                                             data_adimissao = datetime.today(),data_hora_alteracao =datetime.now(),
                                             endereco=result['logradouro'],bairro=result['bairro'],cidade=result['localidade'])
    db.add(novo_func_fab)
    await db.commit()
    
    return novo_func_fab