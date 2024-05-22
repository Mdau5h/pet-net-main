from sqlalchemy.ext.asyncio import AsyncSession
from main.api.models.pets import Pet
from main.serializers.schema import PetRequest


async def create_pet_db(
    request_pet: PetRequest,
    session: AsyncSession
):
    pet = Pet(
        full_name=request_pet.full_name,
        pet_type_id=request_pet.pet_type_id,
        owner_id=request_pet.owner_id
    )
    session.add(pet)
    await session.commit()
    return {
        'id': pet.id,
        'pet': pet.pet_type.title,
        'owner': pet.owner
    }
