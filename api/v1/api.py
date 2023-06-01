from fastapi import APIRouter

from api.v1.endpoints import funcionario_fabrica

api_router = APIRouter()
api_router.include_router(funcionario_fabrica.router, prefix='/funcionario_fabrica',tags=["funcionario_fabrica"])