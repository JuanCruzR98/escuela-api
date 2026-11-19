from sqlalchemy.ext.asyncio import AsyncSession

from app.models.refresh_token import RefreshToken


class RefreshTokenRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        refresh_token: RefreshToken
    ):

        db.add(refresh_token)
        await db.commit()
        await db.refresh(refresh_token)

        return refresh_token