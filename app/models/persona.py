from __future__ import annotations

from datetime import date, datetime
from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, Date, DateTime, CheckConstraint, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database.database import Base

if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.estudiante import Estudiante
    from app.models.docente import Docente
    from app.models.padre import Padre
    from app.models.administrador import Administrativo
    from app.models.telefono import Telefono
    from app.models.correo import Correo
    from app.models.direccion import Direccion

class Persona(Base):
    __tablename__ = "persona"

    id_persona: Mapped[int] = mapped_column(primary_key=True)
    uuid_persona: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)

    primer_nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    segundo_nombre: Mapped[Optional[str]] = mapped_column(String(50))
    primer_apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    segundo_apellido: Mapped[Optional[str]] = mapped_column(String(50))

    fecha_nacimiento: Mapped[Optional[date]] = mapped_column(Date)
    sexo: Mapped[Optional[str]] = mapped_column(String(1))
    cedula: Mapped[Optional[str]] = mapped_column(String(16), unique=True)
    cod_persona: Mapped[Optional[str]] = mapped_column(String(20), unique=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Relaciones
    usuario: Mapped[Optional["Usuario"]] = relationship(back_populates="persona", uselist=False)
    estudiante: Mapped[Optional["Estudiante"]] = relationship(back_populates="persona", uselist=False)
    docente: Mapped[Optional["Docente"]] = relationship(back_populates="persona", uselist=False)
    padre: Mapped[Optional["Padre"]] = relationship(back_populates="persona", uselist=False)
    administrativo: Mapped[Optional["Administrativo"]] = relationship(back_populates="persona", uselist=False)

    telefonos: Mapped[List["Telefono"]] = relationship(back_populates="persona")
    correos: Mapped[List["Correo"]] = relationship(back_populates="persona")
    direcciones: Mapped[List["Direccion"]] = relationship(back_populates="persona")

    __table_args__ = (
        CheckConstraint("sexo IN ('M', 'F', 'X')", name="persona_sexo_check"),
    )

