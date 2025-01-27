from dataclasses import dataclass
from typing import TypedDict

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker

import config


@dataclass
class AppContext:
    db_engine: AsyncEngine
    async_session_factory: async_sessionmaker
    settings: config.Settings


class State(TypedDict):
    app_context: AppContext | None


class Message(BaseModel):
    message: str | None

