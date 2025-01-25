import logfire
from fastapi import FastAPI

from app.core.settings import settings
from app.lifespan import lifespan
from app.routers.service_routers import router as service_router
from app.routers.v1 import v1router

app = FastAPI(lifespan=lifespan, title=settings.APP_NAME)
app.include_router(service_router)
app.include_router(v1router)

logfire.configure(environment=settings.ENV, send_to_logfire="if-token-present")
logfire.instrument_fastapi(app, excluded_urls=("^https?://health*", "^https?://docs*"))


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
