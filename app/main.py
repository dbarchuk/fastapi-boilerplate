from fastapi import FastAPI

from app.core.settings import settings
from app.lifespan import lifespan

app = FastAPI(lifespan=lifespan, title=settings.APP_NAME)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.reload,
        workers=settings.WORKERS,
        log_level=settings.LOG_LEVEL
    )
