from pydantic import BaseModel


class StandardStatusResponse(BaseModel):
    status: str
    error: str | None = None


class ErrorResponseSchema(BaseModel):
    message: str
