from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session
from core.database2 import Session as Session2

async def get_session() ->Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()
        
async def get_session2() ->Generator:
    session: AsyncSession = Session2()
    
    try:
        yield session
    finally:
        await session.close()