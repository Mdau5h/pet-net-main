from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from main.api.models.base import Base
from config import config


engine = create_async_engine(config.DB_PG_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


def db_transaction(func):
    async def wrapper(*args, session: AsyncSession, **kwargs):
        async with session.begin():
            return await func(*args, session=session, **kwargs)
    return wrapper


@db_transaction
async def db_setup(session) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
