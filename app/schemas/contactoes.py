from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class TelefonoCreate(BaseModel):
    numero: str = Field(..., min_length=7, max_length=20)
    tipo: str = Field(default="celular", pattern="^(celular|casa|trabajo|otro)$")
    es_principal: bool = False


class TelefonoResponse(BaseModel):
    id_telefono: int
    uuid_telefono: UUID
    numero: str
    tipo: str
    es_principal: bool

    model_config = {"from_attributes": True}


class CorreoCreate(BaseModel):
    correo: EmailStr
    tipo: str = Field(default="personal", pattern="^(institucional|personal|trabajo|otro)$")
    es_principal: bool = False


class CorreoResponse(BaseModel):
    id_correo: int
    uuid_correo: UUID
    correo: str
    tipo: str
    es_principal: bool

    model_config = {"from_attributes": True}


class DireccionCreate(BaseModel):
    detalle: str = Field(..., min_length=5)
    municipio_id: Optional[int] = None
    es_principal: bool = False


class DireccionResponse(BaseModel):
    id_direccion: int
    uuid_direccion: UUID
    detalle: str
    municipio_id: Optional[int] = None
    es_principal: bool

    model_config = {"from_attributes": True}