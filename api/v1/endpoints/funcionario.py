from typing import List
from datetime import datetime

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.funcionario import FuncionarioModel
from schemas.funcionario_schema import FuncionarioSchema
from core.deps import get_session


router = APIRouter()

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[FuncionarioSchema])
async def get_funcionarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FuncionarioModel)
        result = await session.execute(query)
        funcionarios_fab: List[FuncionarioSchema] = result.scalars().all()
    
        return funcionarios_fab
