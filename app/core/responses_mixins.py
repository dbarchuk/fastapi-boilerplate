from functools import lru_cache
from typing import Any

from app.schemas.service_schemas import ErrorResponseSchema


class ErrorResponse:

    def __init__(self, is_authorized: bool = False):
        self.is_authorized = is_authorized

        self.unauthorized_response = {
            401: {"model": ErrorResponseSchema, "description": "Unauthorized request"},
            403: {"model": ErrorResponseSchema, "description": "Access denied"}
        }
        self.not_found_response = {404: {"model": ErrorResponseSchema, "description": "Not found"}}
        self.bad_request_response = {400: {"model": ErrorResponseSchema, "description": "Bad request"}}

    @property
    def list(self) -> dict[int, Any]:
        if self.is_authorized:
            return self.unauthorized_response
        return {}

    @property
    def retrieve(self) -> dict[int, Any]:
        if self.is_authorized:
            return self.unauthorized_response | self.not_found_response
        return self.not_found_response

    @property
    def create(self) -> dict[int, Any]:
        if self.is_authorized:
            return self.unauthorized_response | self.bad_request_response
        return self.bad_request_response


@lru_cache
def get_authorized_responses() -> ErrorResponse:
    return ErrorResponse(is_authorized=True)


@lru_cache
def get_unauthorized_responses() -> ErrorResponse:
    return ErrorResponse(is_authorized=False)


authorized_responses: ErrorResponse = get_authorized_responses()
unauthorized_responses: ErrorResponse = get_unauthorized_responses()
