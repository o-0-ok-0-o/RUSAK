from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.demo_auto_crud import demo_m2m, get_cars_with_all
from api_v1.crud.salone_member import get_all_salone_members
from api_v1.crud.engine import get_all_engines
from api_v1.crud.salone_option import get_all_salone_options
from api_v1.crud.service import get_all_services
from api_v1.crud.shassi import get_all_shassis
from api_v1.crud.zip import get_all_zips
from db.database import get_async_session
from api_v1.schemas.schemas import (
    CarRead,
    EngineRead,
    SaloneMemberRead,
    SaloneOptionRead,
    ServiceRead,
    ShassiRead,
    ZipRead,
    CarBase,
)

router = APIRouter(
    prefix="/test-crud",
    tags=["Тестовые"],
)


@router.get("/engine", response_model=list[EngineRead])
async def get_engines(
    session: AsyncSession = Depends(get_async_session),
):
    engines = await get_all_engines(session)
    return engines


@router.get("/salone-member", response_model=list[SaloneMemberRead])
async def get_salone_members(
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await get_all_salone_members(session)
    return salone_member


@router.get("/salone-option", response_model=list[SaloneOptionRead])
async def get_salone_option(
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await get_all_salone_options(session)
    return salone_option


@router.get("/service", response_model=list[ServiceRead])
async def get_service(
    session: AsyncSession = Depends(get_async_session),
):
    service = await get_all_services(session)
    return service


@router.get("/shassi", response_model=list[ShassiRead])
async def get_shassi(
    session: AsyncSession = Depends(get_async_session),
):
    shassis = await get_all_shassis(session)
    return shassis


@router.get("/zip", response_model=list[ZipRead])
async def get_zip(
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await get_all_zips(session)
    return zip1


@router.get("/car", response_model=list[CarRead])
async def get_car(
    session: AsyncSession = Depends(get_async_session),
):
    cars = await get_cars_with_all(session)
    return cars
