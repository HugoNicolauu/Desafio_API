from typing import List

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.funcionario_fabrica import Funcionario_fabricaModel
from models.funcionario import FuncionarioModel
from schemas.funcionario_fabrica_schema import Funcionario_FabricaSchema
from core.deps import get_session, get_session2

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED,response_class=Funcionario_FabricaSchema)
async def post_funcionario_fabrica(funcionario:Funcionario_FabricaSchema,db: AsyncSession = Depends(get_session2)):
    pass