from fastapi import APIRouter

from app.schemas.service_schemas import ErrorResponseSchema

router = APIRouter(tags=["Service"])


@router.get("/health", status_code=200, response_model=ErrorResponseSchema)
async def health():
    return {"message": "Ok"}
