from datetime import datetime

from pydantic import UUID4
from sqlalchemy import BIGINT, DateTime, text
from sqlalchemy.orm import Mapped, declarative_mixin, mapped_column
from sqlalchemy.types import Uuid


@declarative_mixin
class UUIDMixin:
    id: Mapped[UUID4] = mapped_column(
        Uuid,
        primary_key=True,
        init=False,
        server_default=text("gen_random_uuid()")
    )


@declarative_mixin
class IntIDMixin:
    id: Mapped[int] = mapped_column(BIGINT,primary_key=True)

@declarative_mixin
class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("timezone('utc', now())"))


@declarative_mixin
class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=text("timezone('utc', now())"), nullable=True)


@declarative_mixin
class CreatedAtUpdatedAtMixin(CreatedAtMixin, UpdatedAtMixin):
    ...
