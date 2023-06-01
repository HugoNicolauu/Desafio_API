from core.configs import settings
from core.database2 import engine as engine2


async def create_tablebd2()-> None:
    import models.funcionario_fabrica
    
    print("Criando A tabela Funcionario_Fabrica No BD2")
    
    async with engine2.begin() as conn2:
        await conn2.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn2.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabela Criada Com sucesso...")
    
if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tablebd2())