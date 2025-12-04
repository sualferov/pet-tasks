import os
from collections.abc import AsyncIterator, Iterable
from contextlib import asynccontextmanager
from typing import Any

import asyncpg
from asyncpg import Connection, Pool, Record
from dotenv import dotenv_values


class Postgres:
    """Класс по работе с PostgresSQl."""

    def __init__(self, dsn: str | None = None):
        self.dsn = dsn
        self.pool = None

    async def _ensure_pool(self) -> Pool:
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.dsn)
        return self.pool

    @asynccontextmanager
    async def _connection(self) -> AsyncIterator[Connection]:
        pool = await self._ensure_pool()
        connection = await pool.acquire()
        try:
            yield connection
        finally:
            await pool.release(connection)

    async def fetch(
        self,
        query: str,
        args: Iterable[object],
        timeout: float | None = None,
    ) -> list[Record]:
        """Возвращает список строк."""
        async with self._connection() as conn:
            return await conn.fetch(query, *args, timeout=timeout)  # type: ignore

    async def fetchrow(
        self,
        query: str,
        args: Iterable[object],
        timeout: float | None = None,
    ) -> Record | None:
        """Возвращает список строк."""
        async with self._connection() as conn:
            return await conn.fetchrow(query, *args, timeout=timeout)

    async def fetchval(  # type: ignore
        self,
        query: str,
        args: Iterable[object],
        timeout: float | None = None,
    ) -> Any:
        """Возвращает список строк."""
        async with self._connection() as conn:
            return await conn.fetchval(query, *args, timeout=timeout)

    async def execute(
        self,
        query: str,
        args: Iterable[object],
        timeout: float | None = None,
    ) -> None:
        """Возвращает список строк."""
        async with self._connection() as conn:
            await conn.execute(query, *args, timeout=timeout)


config = dotenv_values(os.environ.get('ENV_FILE'))
postgres_db = Postgres(dsn=config.get('PG_CONNECTION_DSN'))
