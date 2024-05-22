from sqlalchemy.orm import Session

from . import models, schemas


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Posts).offset(skip).limit(limit).all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Posts).get(post_id)


def create_post(db: Session, item: schemas.CreatePost):
    db_item = models.Posts(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
