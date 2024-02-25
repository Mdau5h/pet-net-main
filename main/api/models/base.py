import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseMixin:
    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
