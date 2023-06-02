from fastapi import APIRouter

from api.v1.endpoints import funcionario_fabrica
from api.v1.endpoints import funcionario

api_router = APIRouter()
api_router.include_router(funcionario_fabrica.router, prefix='/funcionario_fabrica',tags=["Funcionario_Fabrica"])
api_router.include_router(funcionario.router,prefix='/funcionario',tags=["Funcionario"])