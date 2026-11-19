from __future__ import annotations

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, DateTime, ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.municipio import Municipio
    from app.models.persona import Persona

class Direccion(Base):
    __tablename__ = "direcciones"

    id_direccion: Mapped[int] = mapped_column(primary_key=True)
    uuid_direccion: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    persona_id: Mapped[int] = mapped_column(ForeignKey("persona.id_persona", ondelete="CASCADE"), nullable=False)
    municipio_id: Mapped[Optional[int]] = mapped_column(ForeignKey("municipios.id_municipio", ondelete="SET NULL"))
    detalle: Mapped[str] = mapped_column(Text, nullable=False)
    es_principal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    persona: Mapped["Persona"] = relationship(back_populates="direcciones")
    municipio: Mapped[Optional["Municipio"]] = relationship(back_populates="direcciones")