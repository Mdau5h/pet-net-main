from sqlalchemy import (
    Column,
    String,
    LargeBinary
)
from main.api.models.base import Base, BaseMixin


class User(BaseMixin, Base):
    __tablename__ = 'user'

    full_name = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(255), default='')
    login = Column(String(255), nullable=False, unique=True)
    password = Column(LargeBinary(255), nullable=False)
