from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes import PostScheme
from models import get_session
from crud import post, get_all, get
from fastapi import Depends

app = FastAPI()


@app.post("/note/post", summary="Новая заметка")
async def note_post(post_scheme: PostScheme, session: AsyncSession = Depends(get_session)):
    note = await post(post_scheme=post_scheme, session=session)
    return {"message":"Всё в порядке", "note":note.title}

@app.get("/note/get", summary="Все заметки")
async def note_get(session: AsyncSession = Depends(get_session)):
    notes = await get_all(session=session)
    if not notes:
        raise HTTPException(status_code=404, detail="Ошибка")
    return {"message":"Всё в порядке", "notes":notes}


@app.get("/note/get/{note_id}", summary="Заметка с конкретным id")
async def note_get(note_id: int, session: AsyncSession = Depends(get_session)):
    note = await get(id=note_id, session=session)
    if not note:
        raise HTTPException(status_code=404, detail=f"Записи с id {note_id} нет")
    return {"message":"Всё в порядке", "notes":note}