from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.usuario import Usuario
from app.models.persona import Persona
from app.models.correo import Correo    


class UsuarioRepository:

    @staticmethod
    async def get_login_user(
        db: AsyncSession,
        username: str
    ) -> Usuario | None:

        result = await db.execute(
            select(Usuario).where(
                Usuario.username == username,
                Usuario.estado.is_(True),
                Usuario.deleted_at.is_(None)
            )
        )

        return result.scalar_one_or_none()
    
  


async def validate_recovery_user(
    self,
    db: AsyncSession,
    username: str,
    email: str
):
    
    result = await db.execute(
        select(Usuario)
        .join(Usuario.persona)
        .join(Persona.correos)
        .where(
            Usuario.username == username,
            Correo.correo == email,
            Usuario.estado.is_(True),
            Usuario.deleted_at.is_(None)
        )
        .options(
            selectinload(Usuario.persona)
            .selectinload(Persona.correos)
        )
    )

    return result.scalar_one_or_none()