from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.municipio import Municipio
    from app.models.grupo_clase import GrupoClase
    from app.models.matricula import Matricula
    
class AnioAcademico(Base):
    __tablename__ = "anios_academicos"

    id_anio: Mapped[int] = mapped_column(primary_key=True)
    uuid_anio: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[date] = mapped_column(Date, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    grupos: Mapped[List["GrupoClase"]] = relationship(back_populates="anio")
    matriculas: Mapped[List["Matricula"]] = relationship(back_populates="anio")

    __table_args__ = (
        CheckConstraint("fecha_fin > fecha_inicio", name="anios_academicos_check"),
    )