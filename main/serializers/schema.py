from pydantic import BaseModel, Field, EmailStr


class Owner(BaseModel):
    full_name: str = Field(..., alias='fullName', example='Иванов Иван Иванович')
    phone: str = Field(..., alias='phone', pattern=r'^\d{10,}$', min_length=10, max_length=10)
    email: EmailStr = Field('', alias='email', example='test@mail.com')


class PetRequest(BaseModel):
    full_name: str = Field(..., alias='fullName', example='Шарик')
    pet_type_id: int = Field(..., alias='petTypeId')
    owner_id: int = Field(..., alias='ownerId')


class PetResponse(BaseModel):
    id: int
    pet_type: str = Field(..., alias='petTypeId')
    owner: Owner
