from fastapi import APIRouter
from pydantic import UUID4

from app.core.responses_mixins import authorized_responses, unauthorized_responses
from app.schemas.v1.users_schemas import BriefUserResponseSchema, CreateUserSchema

router = APIRouter(prefix="/users")


@router.get("/", responses=authorized_responses.list)
async def get_users():
    return ["Alice", "Bob", "Charlie"]


@router.get("/{user_id}", responses=authorized_responses.retrieve)
async def get_user_by_id(user_id: UUID4):
    return str(user_id)


@router.post("/", responses=unauthorized_responses.create, response_model=BriefUserResponseSchema, status_code=201)
async def create_user(user_data: CreateUserSchema):
    new_user = user_data.model_dump()
    new_user["id"] = "6979a6f8-0cbb-4ec2-851b-90009051c550"
    return new_user
