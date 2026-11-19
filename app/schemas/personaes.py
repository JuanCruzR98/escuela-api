from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, field_validator


class PersonaBase(BaseModel):
    primer_nombre: str = Field(..., min_length=1, max_length=50)
    segundo_nombre: Optional[str] = Field(None, max_length=50)
    primer_apellido: str = Field(..., min_length=1, max_length=50)
    segundo_apellido: Optional[str] = Field(None, max_length=50)
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = Field(None, max_length=1)
    cedula: Optional[str] = Field(None, max_length=16)
    cod_persona: Optional[str] = Field(None, max_length=20)

    @field_validator("sexo")
    @classmethod
    def validar_sexo(cls, v):
        if v is not None and v not in ("M", "F", "X"):
            raise ValueError("Sexo debe ser M, F o X")
        return v


class PersonaCreate(PersonaBase):
    pass


class PersonaUpdate(BaseModel):
    primer_nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    segundo_nombre: Optional[str] = Field(None, max_length=50)
    primer_apellido: Optional[str] = Field(None, min_length=1, max_length=50)
    segundo_apellido: Optional[str] = Field(None, max_length=50)
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = Field(None, max_length=1)
    cedula: Optional[str] = Field(None, max_length=16)
    cod_persona: Optional[str] = Field(None, max_length=20)


class PersonaResponse(PersonaBase):
    id_persona: int
    uuid_persona: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}