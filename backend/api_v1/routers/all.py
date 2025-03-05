from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session

from api_v1.crud.create_engine import get_all_engines
from api_v1.schemas.schemas import (
    CarRead,
    EngineRead,
    SaloneMemberRead,
    SaloneOptionRead,
    ServiceRead,
    ShassiRead,
    ZipRead,
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
def get_colors():
    return 1


@router.get("/salone-option", response_model=list[SaloneOptionRead])
def get_engines():
    return 1


@router.get("/service", response_model=list[ServiceRead])
def get_extras():
    return 1


@router.get("/shassi", response_model=list[ShassiRead])
def get_extras():
    return 1


@router.get("/zip", response_model=list[ZipRead])
def get_extras():
    return 1


@router.get("/car", response_model=list[CarRead])
def get_extras():
    return 1
