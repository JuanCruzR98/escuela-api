from __future__ import annotations

from datetime import date, datetime
from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, Date, DateTime, CheckConstraint, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.persona import Persona


class Administrativo(Base):
    __tablename__ = "administrativos"

    id_administrativo: Mapped[int] = mapped_column(primary_key=True)
    uuid_administrativo: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    persona_id: Mapped[int] = mapped_column(ForeignKey("persona.id_persona", ondelete="CASCADE"), unique=True, nullable=False)
    codigo_administrativo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    cargo: Mapped[str] = mapped_column(String(100), nullable=False)
    tareas: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    persona: Mapped["Persona"] = relationship(back_populates="administrativo")