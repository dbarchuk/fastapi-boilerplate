from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application lifespan")
    try:
        yield
    except Exception as e:
        logger.error(f"Error in application lifespan: {str(e)}")
    finally:
        logger.info("Stopping application lifespan")
