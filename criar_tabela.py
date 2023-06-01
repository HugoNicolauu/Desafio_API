from core.configs import settings
from core.database import engine

async def create_tablebd1()-> None:
    import models.funcionario
    
    print("Criando A tabela Funcionario No BD1")
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabela Criada Com sucesso...")
    
if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tablebd1())
    
    