from pydantic import BaseModel, Field


class PostScheme(BaseModel):
    title: str = Field(max_length=30, min_length=1)
    content: str = Field(max_length=150, min_length=1)