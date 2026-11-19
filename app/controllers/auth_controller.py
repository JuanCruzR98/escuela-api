from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.auth_service import AuthService


class AuthController:

    @staticmethod
    async def login(
        data,
        response,
        db: AsyncSession
    ):
        return await AuthService.login(
            data,
            response,
            db
        )