from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from .database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    text = Column(String, index=True)
    date = Column(Date, index=True)
    time = Column(Time, index=True)
