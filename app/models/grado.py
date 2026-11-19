from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, SmallInteger, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.grupo_clase import GrupoClase
    

class Grado(Base):
    __tablename__ = "grados"

    id_grado: Mapped[int] = mapped_column(primary_key=True)
    uuid_grado: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    nivel: Mapped[str] = mapped_column(nullable=False)  # modalidad enum
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    orden: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    grupos: Mapped[List["GrupoClase"]] = relationship(back_populates="grado")

    __table_args__ = (
        UniqueConstraint("nivel", "nombre", name="grados_nivel_nombre_key"),
        UniqueConstraint("nivel", "orden", name="grados_nivel_orden_key"),
    )