from datetime import date

from models import NotesModel
from sqlalchemy.ext.asyncio import AsyncSession



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
    