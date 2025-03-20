from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.car import get_all_cars
from db.database import get_async_session
from api_v1.schemas.car import CarBase, CarRead

# from db.database import SessionDep, get_session


router = APIRouter(
    prefix="/cars",
    tags=["Машины"],
)


# @router.post("", response_model=CarBase)
# async def create_car_api(
#     car: Annotated[CarBase, Depends()],
#     engine_id: int,
#     salone_member_id: int,
#     tire_id: int,
#     wheelbase_id: int,
#     salone_option_ids: list[int] = Query(..., description="Список ID опций салона"),
#     service_ids: list[int] = Query(..., description="Список ID опций сервиса"),
#     shassi_ids: list[int] = Query(..., description="Список ID опций шасси"),
#     zip_ids: list[int] = Query(..., description="Список ID опций зипа"),
#     file: UploadFile = File(),
#     session: AsyncSession = Depends(get_async_session),
# ):
#     engine = await create_engine(
#         engine=engine,
#         photo=file,
#         session=session,
#     )
#     return engine


# @router.get("/{engine_id}", response_model=CarCar)
# async def get_engine_api(
#     engine_id: int,
#     session: AsyncSession = Depends(get_async_session),
# ):
#     engine = await get_engine(engine_id, session)
#     return engine


#
@router.get("", response_model=list[CarRead])
async def get_all_cars_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    cars = await get_all_cars(
        session,
        offset=offset,
        limit=limit,
    )
    return cars


# @router.get("/{engine_id}/price")
# async def get_engine_price_api(
#     engine_id: int,
#     session: AsyncSession = Depends(get_async_session),
# ):
#     engine_price = await get_engine_price(engine_id, session)
#     return {"engine_price": engine_price}
#
#
# @router.delete("/{engine_id}")
# async def delete_engine_api(
#     engine_id: int,
#     session: AsyncSession = Depends(get_async_session),
# ):
#     engine = await delete_engine(engine_id, session)
#     return engine
