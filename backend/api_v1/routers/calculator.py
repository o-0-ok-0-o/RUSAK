from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.schemas.schemas import CalculatorBase

from db.database import get_async_session
from utils.calculate_price import calculate_price

router = APIRouter(
    prefix="/calculator",
    tags=["Калькулятор"],
)


@router.post("", response_model=CalculatorBase)
async def calculate_all_price(
    engine_id: int,
    salone_member_id: int,
    salone_option_ids: list[int] = Query(..., description="Список ID опций салона"),
    service_ids: list[int] = Query(..., description="Список ID опций сервиса"),
    shassi_ids: list[int] = Query(..., description="Список ID опций шасси"),
    zip_ids: list[int] = Query(..., description="Список ID опций зипа"),
    session: AsyncSession = Depends(get_async_session),
):
    result = await calculate_price(
        session=session,
        engine_id=engine_id,
        salone_member_id=salone_member_id,
        salone_option_ids=salone_option_ids,
        service_ids=service_ids,
        shassi_ids=shassi_ids,
        zip_ids=zip_ids,
    )
    return result
