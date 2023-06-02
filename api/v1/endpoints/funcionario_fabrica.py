from typing import List
from datetime import datetime

from fastapi import APIRouter, status, Depends, HTTPException,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.funcionario_fabrica import Funcionario_fabricaModel
from schemas.funcionario_fabrica_schema import Funcionario_FabricaSchema, Funcionario_FabricaSchemaBase, Funcionario_FabricaSchemaUp
from core.deps import get_session2
from utils.cep_busca import busca_cep

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=Funcionario_FabricaSchema)
async def post_funcionario_fabrica(func_fab:Funcionario_FabricaSchemaBase,db: AsyncSession = Depends(get_session2)):
    result= busca_cep(func_fab.cep)
    novo_func_fab:Funcionario_fabricaModel = Funcionario_fabricaModel(nome=func_fab.nome,rg=func_fab.rg,
                                             cpf=func_fab.cpf,cep=func_fab.cep,
                                             data_adimissao =datetime.now(),
                                             data_hora_alteracao =datetime.today(),
                                             endereco=result['logradouro'],bairro=result['bairro'],cidade=result['localidade'])
    db.add(novo_func_fab)
    async with db as session:
        try:
            await session.commit()
            return novo_func_fab
        except TypeError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail='Dados invalidos')


@router.get('/',response_model=List[Funcionario_FabricaSchema],status_code=status.HTTP_200_OK)
async def get_funcionarios_fabrica(db: AsyncSession = Depends(get_session2)):
    async with db as session:
        query = select(Funcionario_fabricaModel)
        result = await session.execute(query)
        funcionarios_fab: List[Funcionario_FabricaSchema] = result.scalars().all()
    
        return funcionarios_fab
    

@router.get('/{func_fab_id}',response_model=Funcionario_FabricaSchema,status_code=status.HTTP_200_OK)
async def get_funcionario_fabrica(func_fab_id: int, db: AsyncSession = Depends(get_session2)):
    async with db as session:
        query = select(Funcionario_fabricaModel).filter(Funcionario_fabricaModel.id == func_fab_id)
        result = await session.execute(query)
        funcionario_fab: List[Funcionario_FabricaSchema] = result.scalars().one_or_none()
        
        if funcionario_fab:
            return funcionario_fab
        else:
            raise HTTPException(detail='Funcionario Não Encontrado',status_code=status.HTTP_404_NOT_FOUND)
        
        
@router.put('/{func_fab_id}',response_model=Funcionario_FabricaSchema,status_code=status.HTTP_202_ACCEPTED)
async def put_funcionario_fabrica(func_fab_id: int,func_fab:Funcionario_FabricaSchemaUp ,db: AsyncSession = Depends(get_session2)):
    async with db as session:
        query = select(Funcionario_fabricaModel).filter(Funcionario_fabricaModel.id == func_fab_id)
        result = await session.execute(query)
        funcionarios_fab_up: List[Funcionario_FabricaSchema] = result.scalars().one_or_none()
        
        if funcionarios_fab_up:
            if func_fab:
                if func_fab.nome:
                    funcionarios_fab_up.nome=func_fab.nome
                if func_fab.rg:
                    funcionarios_fab_up.rg=func_fab.rg
                if func_fab.cpf:
                    funcionarios_fab_up.cpf=func_fab.cpf
                if func_fab.cep:
                    result= busca_cep(func_fab.cep)
                    funcionarios_fab_up.cep=func_fab.cep
                    funcionarios_fab_up.endereco = result['logradouro']
                    funcionarios_fab_up.bairro = result['bairro']
                    funcionarios_fab_up.cidade = result['localidade']
                    
                funcionarios_fab_up.data_hora_alteracao = datetime.today()
                
            await session.commit()    
            
            return funcionarios_fab_up
        else:
            raise HTTPException(detail='Funcionario Não Encontrado',status_code=status.HTTP_404_NOT_FOUND)       


@router.delete('/{func_fab_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_funcionario_fabrica(func_fab_id: int, db: AsyncSession = Depends(get_session2)):
    async with db as session:
        query = select(Funcionario_fabricaModel).filter(Funcionario_fabricaModel.id == func_fab_id)
        result = await session.execute(query)
        funcionario_fab: List[Funcionario_FabricaSchema] = result.scalars().one_or_none()
        
        if funcionario_fab:
            await session.delete(funcionario_fab)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Funcionario Não Encontrado',status_code=status.HTTP_404_NOT_FOUND)
        

@router.post('/',List[Funcionario_FabricaSchema],status_code=status.HTTP_201_CREATED)
async def transferencia_funcionario(db: AsyncSession = Depends(get_session2)):
    async with db as session:
        pass
            
       