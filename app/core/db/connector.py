from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker

from app.core.logger import get_logger
from app.core.settings import settings

logger = get_logger(__name__)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


DATABASE_URI = settings.postgres_uri

async_engine = create_async_engine(DATABASE_URI, echo=settings.POSTGRES_ECHO)
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)

sync_engine = create_engine(settings.postgres_uri_sync, echo=settings.POSTGRES_ECHO)
sync_session = sessionmaker(sync_engine)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def check_database_connection() -> None:
    try:
        async with async_session() as session:
            await session.execute(text("SELECT * FROM pg_stat_activity;"))
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Error in database connection: {str(e)}")
        raise e
