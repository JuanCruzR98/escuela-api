from __future__ import annotations

from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, CITEXT

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.municipio import Municipio
    from app.models.persona import Persona

class Departamento(Base):
    __tablename__ = "departamentos"

    id_departamento: Mapped[int] = mapped_column(primary_key=True)
    uuid_departamento: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    nombre: Mapped[str] = mapped_column(CITEXT, unique=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))

    municipios: Mapped[List["Municipio"]] = relationship(back_populates="departamento")