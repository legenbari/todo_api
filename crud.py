from datetime import date

from fastapi import HTTPException

from models import NotesModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select



async def post(post_scheme, session: AsyncSession):
    new_note = NotesModel(
        title=post_scheme.title,
        content=post_scheme.content,
        date=date.today()  
    )
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note

async def get_all(session: AsyncSession):
    result = await session.execute(select(NotesModel))
    return result.scalars().all()

async def get(id, session: AsyncSession):
    result = await session.execute(select(NotesModel).where(NotesModel.id==id))
    return result.scalars().all()
