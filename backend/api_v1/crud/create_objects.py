from os import times_result

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import (
    Car,
    Engine,
    SaloneMember,
    SaloneOption,
    Service,
    Shassi,
    Zip,
    Tire,
)


async def create_car(
    car_name: str,
    base_price: int,
    engine_id: int,
    salone_member_id: int,
    tire_id,
    session: AsyncSession,
) -> Car:
    car = Car(
        car_name=car_name,
        base_price=base_price,
        engine_id=engine_id,
        salone_member_id=salone_member_id,
        tire_id=tire_id,
    )
    session.add(car)
    await session.commit()
    return car


async def create_engine(
    engine_name: str,
    base_price: int,
    session: AsyncSession,
) -> Engine:
    engine = Engine(
        engine_name=engine_name,
        base_price=base_price,
    )
    session.add(engine)
    await session.commit()
    return engine


async def create_tire(
    tire_name: str,
    base_price: int,
    session: AsyncSession,
) -> Tire:
    tire = Tire(
        tire_name=tire_name,
        base_price=base_price,
    )
    session.add(tire)
    await session.commit()
    return tire


async def create_salonemember(
    salone_name: str,
    base_price: int,
    session: AsyncSession,
) -> SaloneMember:
    salone_member = SaloneMember(
        salone_name=salone_name,
        base_price=base_price,
    )

    session.add(salone_member)
    await session.commit()
    return salone_member


async def create_saloneoption(
    salone_option_name: str,
    base_price: int,
    session: AsyncSession,
) -> SaloneOption:
    salone_option = SaloneOption(
        salone_option_name=salone_option_name,
        base_price=base_price,
    )

    session.add(salone_option)
    await session.commit()
    return salone_option


async def create_service(
    service_name: str,
    base_price: int,
    session: AsyncSession,
) -> Service:
    service = Service(
        service_name=service_name,
        base_price=base_price,
    )

    session.add(service)
    await session.commit()
    return service


async def create_shassi(
    shassi_name: str,
    base_price: int,
    session: AsyncSession,
) -> Shassi:
    shassi = Shassi(
        shassi_name=shassi_name,
        base_price=base_price,
    )
    session.add(shassi)
    await session.commit()
    return shassi


async def create_zip(
    zip_name: str,
    base_price: int,
    session: AsyncSession,
) -> Zip:
    zip1 = Zip(
        zip_name=zip_name,
        base_price=base_price,
    )
    session.add(zip1)
    await session.commit()
    return zip1
