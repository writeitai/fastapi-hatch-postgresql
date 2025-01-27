from enum import Enum

from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic import Field


class AppEnvironment(str, Enum):
    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings):
    # dev | prod - the environment the app is running in
    env: AppEnvironment = Field(default=AppEnvironment.DEV)

    # the port the server listens on
    listen_port: str = Field(default="8080")

    # the host the server listens on
    listen_host: str = Field(default="127.0.0.1")

    # the postgres uri for the app
    default_postgres_uri: str = Field(default="postgresql+asyncpg://trusted_user:trusted_user_password@localhost:5432/dev_db")

    # the postgres uri used during testing
    test_postgres_uri: str = Field(default="postgresql+asyncpg://trusted_user:trusted_user_password@localhost:5432/test_db")

    class Config:
        # The prefix for environment variables
        env_prefix = "SERVER_"
        # revalidates the instance during validation (when model_validate is called)
        revalidate_instances = "always"
        env_file = "../.env"


@lru_cache()
def get_settings() -> Settings:
    """
    Returns the app settings Pydantic class.
    The lru_cache decorator caches settings so that they are only loaded once.
    The pattern was taken from FASTAPI docs: https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
    """
    return Settings()
