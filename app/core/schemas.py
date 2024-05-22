from datetime import datetime

from pydantic import BaseModel


class PostsBase(BaseModel):
    title: str
    text: str


class CreatePost(PostsBase):
    date: str = datetime.now().date()
    time: str = datetime.now().time()


class Post(CreatePost):
    id: int

    class Config:
        orm_mode = True
