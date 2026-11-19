from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from app.schemas.personaes import PersonaCreate, PersonaResponse


class PadreCreate(BaseModel):
    persona: PersonaCreate


class PadreResponse(BaseModel):
    id_padre: int
    uuid_padre: UUID
    persona: PersonaResponse
    created_at: datetime

    model_config = {"from_attributes": True}