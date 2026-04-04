from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, TEXT, DATE, INTEGER
from config import PASSWORD, LOGIN, DB_NAME, HOST, PORT

url = f"postgresql+asyncpg://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_async_engine(url=url, echo=True)
Base = declarative_base()

class NotesModel(Base):
    __tablename__ = "notes"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(TEXT)
    content = Column(TEXT)
    date = Column(DATE)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session