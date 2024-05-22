from sqlalchemy.ext.asyncio import AsyncSession
from main.api.v1.db_controllers import create_pet_db
from main.app.db import db_transaction
from main.serializers.schema import PetRequest


@db_transaction
async def create_pet(request_params: PetRequest, session: AsyncSession):
    try:
        return await create_pet_db(request_params, session=session)
    except Exception as e:
        raise e
