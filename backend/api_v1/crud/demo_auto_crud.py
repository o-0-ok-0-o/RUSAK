import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from api_v1.crud.create_objects import (
    create_car,
    create_engine,
    create_salonemember,
    create_saloneoption,
    create_service,
    create_shassi,
    create_zip,
    create_tire,
    create_wheelbase,
)
from db.database import async_session_factory, drop_tables, create_tables
from db.models import Car, Service, SaloneOption, Shassi, Zip


async def create_cars_and_relations(
    session: AsyncSession,
):
    engine_1 = await create_engine("двигатель 1", 1500, session)
    engine_2 = await create_engine("двигатель 2", 2500, session)

    tire_1 = await create_tire("Колесо р18", 1500, session)
    tire_2 = await create_tire("Колесо р25", 2500, session)

    wheelbase_1 = await create_wheelbase("8x8", 1500, session)
    wheelbase_2 = await create_wheelbase("6x6", 2500, session)

    salone_member1 = await create_salonemember("16 мест", 1500, session)
    salone_member2 = await create_salonemember("20 мест", 2200, session)

    salone_option1 = await create_saloneoption("обогрев", 1500, session)
    salone_option2 = await create_saloneoption("задняя камера", 2200, session)

    service1 = await create_service("домкрат", 1500, session)
    service2 = await create_service("инструменты", 3300, session)

    shassi1 = await create_shassi("подкачка колес", 1500, session)
    shassi2 = await create_shassi("колпаки на колеса", 3300, session)

    zip1 = await create_zip("зип стандарт", 1500, session)
    zip2 = await create_zip("зип дополнительный", 3300, session)

    car1 = await create_car(
        car_name="К-8 Грузовой 4х2,5",
        base_price=1_499_000,
        engine_id=engine_1.id,
        salone_member_id=salone_member1.id,
        tire_id=tire_1.id,
        wheelbase_id=wheelbase_1.id,
        session=session,
    )
    car2 = await create_car(
        car_name="К-2 Легковой 5х2,5",
        base_price=2_999_000,
        engine_id=engine_2.id,
        salone_member_id=salone_member2.id,
        tire_id=tire_2.id,
        wheelbase_id=wheelbase_2.id,
        session=session,
    )

    car1 = await session.scalar(
        select(Car)
        .where(Car.id == car1.id)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
        ),
    )
    car2 = await session.scalar(
        select(Car)
        .where(Car.id == car2.id)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
        ),
    )

    car1.salone_option.append(salone_option1)
    car1.service.append(service1)
    car1.shassi.append(shassi1)
    car1.zip.append(zip1)

    car2.salone_option.append(salone_option2)
    car2.service.append(service2)
    car2.shassi.append(shassi2)
    car2.zip.append(zip2)

    await session.commit()


async def get_cars_with_all(session: AsyncSession) -> list[Car]:
    stmt = (
        select(Car)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
            joinedload(Car.salone_member),
            joinedload(Car.engine),
            joinedload(Car.tire),
            joinedload(Car.wheelbase),
        )
        .order_by(Car.id)
    )
    cars = await session.scalars(statement=stmt)

    return list(cars)


async def demo_m2m(session: AsyncSession):
    cars = await get_cars_with_all(session)
    for car in cars:
        print(car.id, car.car_name, car.base_price)
        #
        print(
            "Двигатель:",
            car.engine.engine_name,
            car.engine.base_price,
        )
        print(
            "Вместительность салона:",
            car.salone_member.salone_name,
            car.salone_member.base_price,
        )
        print(
            "Шины:",
            car.tire.tire_name,
            car.tire.base_price,
        )
        print(
            "Колесная база:",
            car.wheelbase.wheelbase_name,
            car.wheelbase.base_price,
        )
        #
        print("Опции салона:")
        for salone_option in car.salone_option:  # type: SaloneOption
            print(salone_option.salone_option_name, salone_option.base_price)
        print("Сервис:")
        for service in car.service:  # type: Service
            print(service.service_name, service.base_price)
        print("Шасси:")
        for shassi in car.shassi:  # type: Shassi
            print(shassi.shassi_name, shassi.base_price)
        print("Зип:")
        for zip1 in car.zip:  # type: Zip
            print(zip1.zip_name, zip1.base_price)


async def main():
    # await drop_tables()
    # await create_tables()
    # async with async_session_factory() as session:
    # await create_cars_and_relations(session)
    # await demo_m2m(session)
    pass


# if __name__ == "__main__":
#     asyncio.run(main())
