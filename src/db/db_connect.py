from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from config import Settings


def get_postgres_uri(settings: Settings) -> str:
    """
    Returns the Postgres URI - reflects benchmark runs and their type.
    """
    return settings.default_postgres_uri


def get_db_engine(settings: Settings):
    """
    Returns the async engine for the Postgres database.
    """
    postgres_uri = get_postgres_uri(settings=settings)
    return create_async_engine(url=postgres_uri, echo=False)


def get_async_sessionmaker(engine: AsyncEngine) -> async_sessionmaker:
    """
    Factory for creating new Session objects.
    """
    # expire_on_commit=False will prevent attributes from being expired after commit.
    return async_sessionmaker(engine, expire_on_commit=False)
