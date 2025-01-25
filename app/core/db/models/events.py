from pydantic import UUID4
from sqlalchemy import JSON, Enum, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.constants import UserEventTypes
from app.core.db.connector import Base
from app.core.db.models.mixins import CreatedAtMixin, IntIDMixin

__all__ = ("UserEvent", )


class UserEvent(Base, IntIDMixin, CreatedAtMixin):
    __tablename__ = "events"

    event_type: Mapped[UserEventTypes] = mapped_column(Enum(UserEventTypes), index=True)
    user_id: Mapped[UUID4] = mapped_column(Uuid)
    additional_data: Mapped[dict] = mapped_column(JSON, nullable=True, default=dict)
