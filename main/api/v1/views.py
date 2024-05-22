from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from main.api.v1.controllers import create_pet
from main.app.db import get_session
from main.serializers.schema import PetRequest, PetResponse

routes = APIRouter()


@routes.post(
    "/",
    response_model=PetResponse,
    status_code=201,
)
async def create_pet_view(
        request_params: PetRequest,
        session: AsyncSession = Depends(get_session)
):
    return await create_pet(request_params=request_params, session=session)
