from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_async_session
from utils.calculate_price import calculate_price

router = APIRouter(
    prefix="/calculator",
    tags=["Калькулятор"],
)


@router.post("")
async def calculate_all_price(session: AsyncSession = Depends(get_async_session)):
    result = await calculate_price(
        session=session,
        engine_id=1,
        salone_member_id=1,
        salone_option_ids=[1, 2],
        service_ids=[1, 2],
        shassi_ids=[1, 2],
        zip_ids=[1, 2],
    )
    return result
