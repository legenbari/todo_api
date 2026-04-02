from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from schemes import PostScheme
from models import get_session
from crud import post
from fastapi import Depends

app = FastAPI()


@app.post("/note/post")
async def note_post(post_scheme: PostScheme, session: AsyncSession = Depends(get_session)):
    note = await post(post_scheme=post_scheme, session=session)
    return {"message":"Всё в порядке", "note":note.title}