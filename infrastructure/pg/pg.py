from typing import Any, Sequence

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from internal.model import DBInterface


def NewPool(db_user, db_pass, db_host, db_port, db_name):
    async_engine = create_async_engine(
        f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}",
        echo=False,
        future=True,
        pool_size=15,
        max_overflow=15,
        pool_recycle=300
    )

    pool = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False
    )
    return pool


class PG(DBInterface):

    def __init__(self, db_user, db_pass, db_host, db_port, db_name):
        self.pool = NewPool(db_user, db_pass, db_host, db_port, db_name)

    async def insert(self, query: str, query_params: dict) -> int:
        try:
            async with self.pool() as session:
                result = await session.execute(text(query), query_params)
                rows = result.all()
                await session.commit()
                return rows[0][0]
        except Exception as e:
            raise e

    async def delete(self, query: str, query_params: dict) -> None:
        try:
            async with self.pool() as session:
                await session.execute(text(query), query_params)
                await session.commit()
        except Exception as e:
            raise e

    async def update(self, query: str, query_params: dict) -> None:
        try:
            async with self.pool() as session:
                await session.execute(text(query), query_params)
                await session.commit()
        except Exception as e:
            raise e

    async def select(self, query: str, query_params: dict) -> Sequence[Any]:
        try:
            async with self.pool() as session:
                result = await session.execute(text(query), query_params)
                await session.commit()
                rows = result.all()
                return rows
        except Exception as e:
            raise e

    async def multi_query(
            self,
            queries: list[str]
    ) -> None:
        async with self.pool() as session:
            for query in queries:
                await session.execute(text(query))
            await session.commit()
        return None
