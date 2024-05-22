from fastapi import APIRouter, Depends

router = APIRouter()

from app.core import models, crud, schemas
from app.core.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db = get_db()


@router.get("/")
def get_all_posts(
    db: SessionLocal = Depends(get_db),
    page_num: int = 1,
    page_size: int = 10,
):
    start = (page_num - 1) * page_size
    return crud.get_posts(db, start, page_size)


@router.get("/{post_id}/")
def get_all_posts(
    post_id: int,
    db: SessionLocal = Depends(get_db),
):
    return crud.get_post_by_id(db, post_id)


@router.post("/", response_model=schemas.PostsBase)
def create_post(post: schemas.CreatePost, db: SessionLocal = Depends(get_db)):

    return crud.create_post(db, post)
