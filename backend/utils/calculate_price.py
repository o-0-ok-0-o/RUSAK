import asyncio

from fastapi import HTTPException, Depends

from api_v1.crud.engine import get_engine_price
from api_v1.crud.salone_member import get_salone_member_price
from api_v1.crud.salone_option import get_salone_option_price
from api_v1.crud.service import get_service_price
from api_v1.crud.shassi import get_shassi_price
from api_v1.crud.zip import get_zip_price
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session


async def calculate_price(
    engine_id: int,
    salone_member_id: int,
    salone_option_ids: list[int],
    service_ids: list[int],
    shassi_ids: list[int],
    zip_ids: list[int],
    session: AsyncSession = Depends(get_async_session),
) -> dict[str, int]:
    try:
        engine_price = await get_engine_price(engine_id, session)
        salone_member_price = await get_salone_member_price(salone_member_id, session)

        salone_options_price = await asyncio.gather(
            *(get_salone_option_price(option_id, session) for option_id in salone_option_ids)
        )
        service_price = await asyncio.gather(
            *(get_service_price(service_id, session) for service_id in service_ids)
        )
        shassi_price = await asyncio.gather(
            *(get_shassi_price(shassi_id, session) for shassi_id in shassi_ids)
        )
        zip_price = await asyncio.gather(
            *(get_zip_price(zip_id, session) for zip_id in zip_ids)
        )

        total_price = (
            engine_price
            + salone_member_price
            + sum(salone_options_price)
            + sum(service_price)
            + sum(shassi_price)
            + sum(zip_price)
        )
        return {
            "engine": engine_price,
            "salone_member": salone_member_price,
            "salone_option's": salone_options_price,
            "service's": service_price,
            "shassi's": shassi_price,
            "zip's": zip_price,
            "total_price":total_price}
    except HTTPException as e:
        raise e

