from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, SmallInteger, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.departamento import Departamento
    from app.models.direccion import Direccion
    
class Municipio(Base):
    __tablename__ = "municipios"

    id_municipio: Mapped[int] = mapped_column(primary_key=True)
    uuid_municipio: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id_departamento", ondelete="RESTRICT"), nullable=False)
    nombre: Mapped[str] = mapped_column(CITEXT, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    departamento: Mapped["Departamento"] = relationship(back_populates="municipios")
    direcciones: Mapped[List["Direccion"]] = relationship(back_populates="municipio")

    __table_args__ = (
        UniqueConstraint("departamento_id", "nombre", name="municipios_departamento_id_nombre_key"),
    )