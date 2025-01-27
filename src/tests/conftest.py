import asyncio
import os

import pytest
import sqlalchemy
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine

import config
from db.db_connect import get_async_sessionmaker
from db.models import Base
from py_models import AppContext


@pytest.fixture(scope="session", autouse=True)
def set_env():
    # set the required environment variables
    os.environ["SERVER_DEFAULT_POSTGRES_URI"] = "test_postgres_string"
    os.environ["SERVER_TEST_POSTGRES_URI"] = (
        "postgresql+asyncpg://trusted_user:trusted_user_password"
        "@localhost:5432/test_db"
    )


@pytest.fixture(scope="session")
def settings():
    return config.get_settings()


@pytest.fixture(scope="session")
def db_engine():
    return create_async_engine(
        # The NullPool due to https://github.com/encode/starlette/issues/1315#issuecomment-1279330380
        url=config.get_settings().test_postgres_uri,
        poolclass=NullPool,
        echo=False,
    )


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """
    Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154
    """  # noqa: E501
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def drop_create_tables(db_engine):
    async with db_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="function", autouse=True)
def refresh_db(db_engine):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(drop_create_tables(db_engine))


@pytest.fixture()
def async_session_factory(db_engine):
    """Returns an async session factory."""
    return sqlalchemy.ext.asyncio.async_sessionmaker(
        bind=db_engine, expire_on_commit=False
    )


@pytest.fixture()
def app_context(settings, db_engine):
    return AppContext(
        settings=settings,
        db_engine=db_engine,
        async_session_factory=get_async_sessionmaker(engine=db_engine),
    )

@pytest.fixture()
def app_state(app_context):
    return {"app_context": app_context}
