from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import select

from app_context import get_app_context
from db.models import ExampleModel
from py_models import Message
from py_models import State


app_state: State = {"app_context": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_context = await get_app_context()
    app_state["app_context"] = app_context

    yield

    # Clean up the app_context and release the resources
    app_state.clear()


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root() -> Message:
    app_context = app_state["app_context"]

    async with app_context.async_session_factory() as session:
        stmt = select(ExampleModel)
        result = await session.execute(stmt)
        example = result.scalars().first()
        message = example.message if example else "No message found"

    return Message(message=message)