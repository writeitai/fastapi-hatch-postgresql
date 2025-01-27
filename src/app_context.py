import config
from db.db_connect import get_async_sessionmaker
from db.db_connect import get_db_engine
from py_models import AppContext


async def get_app_context() -> AppContext:
    # load settings
    settings = config.get_settings()

    # load heavy resources
    db_engine = get_db_engine(settings=settings)
    async_session_factory = get_async_sessionmaker(engine=db_engine)

    app_context = AppContext(
        settings=settings,
        db_engine=db_engine,
        async_session_factory=async_session_factory,
    )

    return app_context
