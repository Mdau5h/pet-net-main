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
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    owner = relationship('Owner')


class PetType(BaseMixin, Base):
    __tablename__ = 'pet_type'

    title = Column(String(255), nullable=False, unique=True)


class Owner(BaseMixin, Base):
    __tablename__ = 'owner'

    full_name = Column(String(255), nullable=False)
    email = Column(String(255), default='')
    login = Column(String(255), nullable=False, unique=True)
