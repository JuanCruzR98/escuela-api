from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True,future=True)

AssyncSessionLocal = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession, 
    autoflush=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AssyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()