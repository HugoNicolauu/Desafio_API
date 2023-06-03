from typing import List
from datetime import datetime

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.funcionario import FuncionarioModel
from schemas.funcionario_schema import FuncionarioSchema
from core.deps import get_session
from utils.log_check import logging,LogCheck,data_limite


router = APIRouter()

@router.get('/',response_model=List[FuncionarioSchema],status_code= status.HTTP_200_OK)
async def get_funcionarios(db: AsyncSession = Depends(get_session)):
    LogCheck(data_limite)
    logging.info("Listando Funcionarios.")
    async with db as session:
        query = select(FuncionarioModel)
        result = await session.execute(query)
        funcionarios: List[FuncionarioSchema] = result.scalars().all()
    
        return funcionarios
