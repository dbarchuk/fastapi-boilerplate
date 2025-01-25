from pydantic import UUID4, BaseModel


class CreateUserSchema(BaseModel):
    name: str
    email: str


class BriefUserResponseSchema(CreateUserSchema):
    id: UUID4
