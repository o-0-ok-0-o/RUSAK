import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from api_v1.crud.create_objects_demo import (
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
    engine_1 = await create_engine(
        "Дизельный Cummins 2,8 л; 110 кВт",
        350000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    engine_2 = await create_engine(
        "Дизельный двигатель WP3NQ160A0",
        420000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    tire_1 = await create_tire(
        "1650x650 R25 RUSAK",
        180000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    tire_2 = await create_tire(
        "1780x710 R32 MAMONT",
        240000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    wheelbase_1 = await create_wheelbase(
        "8x8", 150000, "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png", session
    )
    wheelbase_2 = await create_wheelbase(
        "6x6", 250000, "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png", session
    )

    salone_member_1 = await create_salonemember(
        "18 пассажирских мест",
        120000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_member_2 = await create_salonemember(
        "20 пассажирских мест",
        150000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_member_3 = await create_salonemember(
        "24 пассажирских мест",
        180000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_member_4 = await create_salonemember(
        "28 пассажирских мест",
        210000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    salone_option_1 = await create_saloneoption(
        "Обогрев лобового стекла",
        25000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_option_2 = await create_saloneoption(
        "Задняя камера с монитором 2DIN",
        35000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_option_3 = await create_saloneoption(
        "Автономные отопители салона Планар 4кВт 1 шт, Планар 2кВт 1 шт",
        65000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    salone_option_4 = await create_saloneoption(
        "Радиостанция Hytera HM785 или аналог",
        45000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    shassi_1 = await create_shassi(
        "Централизованная система подкачки колес",
        85000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_2 = await create_shassi(
        "Предпусковой подогреватель двигателя Бинар, 5кВт",
        40000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_3 = await create_shassi(
        "Лебедка передняя Runva 20000 (усилие 9,6 т) с кронштейном",
        75000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_4 = await create_shassi(
        "Кенгурин передний",
        45000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_5 = await create_shassi(
        "Экспедиционный багажник на крыше с поручнями 2,0×1,7 м",
        60000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_6 = await create_shassi(
        "Фара светодиодная РИФ 20'' 120 W LED, крепление в бампере, 2 шт.",
        30000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_7 = await create_shassi(
        "Фара светодиодная РИФ D116 мм 18W c кнопкой включения на панели, 3 шт",
        25000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    shassi_8 = await create_shassi(
        "Колпаки на колеса",
        20000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    service_1 = await create_service(
        "Домкрат Hi-Lift 605 X-Treme (или аналогичный)",
        15000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    service_2 = await create_service(
        'Набор инструментов 150 предметов 1/2" и 3/8" 06-07-21 (крепление в салоне)',
        25000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    service_3 = await create_service(
        "Преобразователь напряжения 12-220 В, 4000 W",
        30000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    service_4 = await create_service(
        "Шланг для подкачки колес",
        5000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    service_5 = await create_service(
        'Полноразмерное запасное колесо 1650х650-25", 4НС',
        45000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    zip_1 = await create_zip(
        "Комплект ЗИП стандартный",
        120000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )
    zip_2 = await create_zip(
        "Комплект ЗИП дополнительный",
        180000,
        "test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        session,
    )

    car_1 = await create_car(
        car_name="К-8 Грузовой 4х2,5",
        base_price=1_499_000,
        photo_url="test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        engine_id=engine_1.id,
        salone_member_id=salone_member_1.id,
        tire_id=tire_1.id,
        wheelbase_id=wheelbase_1.id,
        session=session,
    )
    car_2 = await create_car(
        car_name="К-2 Легковой 5х2,5",
        base_price=2_999_000,
        photo_url="test-photo/3f45254b-567d-4a78-95bf-47a626ead49e.png",
        engine_id=engine_2.id,
        salone_member_id=salone_member_2.id,
        tire_id=tire_2.id,
        wheelbase_id=wheelbase_2.id,
        session=session,
    )

    car_1 = await session.scalar(
        select(Car)
        .where(Car.id == car_1.id)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
        ),
    )
    car_2 = await session.scalar(
        select(Car)
        .where(Car.id == car_2.id)
        .options(
            selectinload(Car.salone_option),
            selectinload(Car.service),
            selectinload(Car.shassi),
            selectinload(Car.zip),
        ),
    )

    car_1.salone_option.append(salone_option_1)
    car_1.service.append(service_1)
    car_1.shassi.append(shassi_1)
    car_1.zip.append(zip_1)

    car_2.salone_option.append(salone_option_2)
    car_2.service.append(service_2)
    car_2.shassi.append(shassi_2)
    car_2.zip.append(zip_2)

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
        print(car.id, car.car_name, car.base_price, car.photo_url)
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
    #     await create_cars_and_relations(session)
    #     await demo_m2m(session)
    pass


# if __name__ == "__main__":
#     asyncio.run(main())
