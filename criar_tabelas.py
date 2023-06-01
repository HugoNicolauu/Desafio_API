from core.configs import settings
from core.database import engine
from core.database2 import engine as engine2

async def create_tablebd1()-> None:
    import models.funcionario
    print("Criando A tabela Funcionario No BD1")
    
    async with engine.begin() as conn:
        await conn.run_async(settings.DBBaseModel.metadata.drop_all)
        await conn.run_async(settings.DBBaseModel.metadata.create_all)
    print("Tabela Criada Com sucesso...")
    
async def create_tablebd2()-> None:
    import models.funcionario_fabrica
    print("Criando A tabela Funcionario_Fabrica No BD2")
    
    async with engine.begin() as conn:
        await conn.run_async(settings.DBBaseModel.metadata.drop_all)
        await conn.run_async(settings.DBBaseModel.metadata.create_all)
    print("Tabela Criada Com sucesso...")
    
if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tablebd1())
    asyncio.run(create_tablebd2())
    