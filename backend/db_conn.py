from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.config import Config

engine = create_async_engine(Config.PG_LINK)
session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> Session:
    async with session() as s:
        try:
            yield s
        finally:
            await s.close()
