from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.db.connector import check_database_connection
from app.core.logger import get_logger
from app.core.settings import settings

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting FastAPI, environment: {settings.ENV}")
    try:
        await check_database_connection()
        yield
    except Exception as e:
        logger.error(f"Error in application lifespan: {str(e)}")
    finally:
        logger.info("Stopping application lifespan")
