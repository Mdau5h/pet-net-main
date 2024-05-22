from sqlalchemy import (
    ForeignKey,
    Column,
    String,
)
from sqlalchemy.orm import relationship
from main.api.models.base import Base, BaseMixin


class Pet(BaseMixin, Base):
    __tablename__ = 'pet'

    full_name = Column(String(255), nullable=False)
    pet_type_id = Column(ForeignKey('pet_type.id'), nullable=False)
    pet_type = relationship('PetType')
    owner_id = Column(ForeignKey('user.id'), nullable=False)
    owner = relationship('User')


class PetType(BaseMixin, Base):
    __tablename__ = 'pet_type'

    title = Column(String(255), nullable=False, unique=True)


