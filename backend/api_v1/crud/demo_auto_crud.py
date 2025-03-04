import asyncio
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, Session
from starlette.responses import JSONResponse

from db.database import async_session_factory, drop_tables, create_tables
from db.models import Engine, SaloneMember, Car, Service, SaloneOption, Shassi, Zip


async def create_car(
    car_name: str,
    base_price: int,
    # engine: Engine,
    # salone_member: SaloneMember,
    session: AsyncSession,
) -> Car:
    car = Car(
        car_name=car_name,
        base_price=base_price,
        # engine_id=engine.id,
        # salone_member=salone_member.id,
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


################################
async def main_relations(
    session: AsyncSession,
):
    # engine_1 = create_engine("двигатель 1", 1500, session)
    # engine_2 = create_engine("двигатель 2", 2500, session)
    #
    # salone_member1 = create_salonemember("16 мест", 1500, session)
    # salone_member2 = create_salonemember("20 мест", 2200, session)

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
        base_price=1_500_000,
        # engine=engine_1,
        # salone_member=salone_member1,
        session=session,
    )
    car2 = await create_car(
        car_name="К-2 Легковой 5х2,5",
        base_price=2_999_000,
        # engine=engine_2,
        # salone_member=salone_member2,
        session=session,
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


def format_car(car: Car) -> dict:
    return {
        "id": car.id,
        "name": car.car_name,
        "base_price": car.base_price,
        # "engine": {
        #     "id": car.engine_id.id,
        #     "name": car.engine_id.engine_name,
        #     "power": car.engine_id.base_price,
        # },
        # "salone_member": {
        #     "id": car.salone_member.id,
        #     "name": car.salone_member.name,
        #     "price": car.salone_member.base_price,
        # },
        "salone_option": [
            {
                "id": option.id,
                "name": option.salone_option_name,
                "price": option.base_price,
            }
            for option in car.salone_option
        ],
        "service": [
            {
                "id": service.id,
                "name": service.service_name,
                "price": service.base_price,
            }
            for service in car.service
        ],
        "shassi": [
            {"id": shassi.id, "name": shassi.shassi_name, "price": shassi.base_price}
            for shassi in car.shassi
        ],
        "zip": [
            {"id": zip1.id, "name": zip1.zip_name, "price": zip1.base_price}
            for zip1 in car.zip
        ],
    }


async def get_car(session: AsyncSession) -> list[Car]:
    stmt = (
        select(Car)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
        )
        .order_by(Car.id)
    )
    cars = await session.scalars(stmt)
    return list(cars)


def print_cars(cars: list[Car]):
    for car in cars:
        car_data = format_car(car)
        print(f"Машина: {car_data['name']}")
        print(f"Базовая цена: {car_data['base_price']}")
        print(
            f"Двигатель: {car_data['engine']['name']} (мощность: {car_data['engine']['power']})"
        )
        print(
            f"Салон: {car_data['salone_member']['name']} (цена: {car_data['salone_member']['price']})"
        )
        print("Опции салона:")
        for option in car_data["salone_options"]:
            print(f"  - {option['name']} (цена: {option['price']})")
        print("Услуги:")
        for service in car_data["services"]:
            print(f"  - {service['name']} (цена: {service['price']})")
        print("Шасси:")
        for shassi in car_data["shassis"]:
            print(f"  - {shassi['name']} (цена: {shassi['price']})")
        print("ZIP-комплекты:")
        for zip1 in car_data["zips"]:
            print(f"  - {zip1['name']} (цена: {zip1['price']})")
        print("-" * 40)


async def demo_m2m(session: AsyncSession):
    # await main_relations(session)
    cars = await get_car(session)
    formatted_cars = [format_car(car) for car in cars]
    print(formatted_cars)


async def main():
    # await drop_tables()
    # await create_tables()
    async with async_session_factory() as session:
        await demo_m2m(session)


asyncio.run(main())
