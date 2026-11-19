from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.docente_especialidad import DocenteEspecialidad
    
class Especialidad(Base):
    __tablename__ = "especialidades"

    id_especialidad: Mapped[int] = mapped_column(primary_key=True)
    uuid_especialidad: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    docentes_rel: Mapped[List["DocenteEspecialidad"]] = relationship(back_populates="especialidad")