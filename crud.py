from datetime import date

from fastapi import HTTPException

from models import NotesModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete



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

async def put(id, session:AsyncSession, post_scheme):
    upd = update(NotesModel).where(NotesModel.id == id).values(**post_scheme.dict()).returning(NotesModel)
    result = await session.execute(upd)
    await session.commit()
    return result.scalar_one_or_none()

async def delete_note(id, session:AsyncSession):
    del_note = delete(NotesModel).where(NotesModel.id == id).returning(NotesModel)
    result = await session.execute(del_note)
    await session.commit()
    return result.scalar_one_or_none()