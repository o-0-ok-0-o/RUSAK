import asyncio
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, Session

from db.database import get_session, SessionDep
from db.models import Engine, SaloneMember, Car, Service, SaloneOption, Shassi, Zip


def create_car(
    car_name: str,
    base_price: int,
    engine: Engine,
    salone_member: SaloneMember,
    session: Session,
) -> Car:
    car = Car(
        car_name=car_name,
        base_price=base_price,
        engine_id=engine.id,
        salone_member=salone_member.id,
    )
    session.add(car)
    session.commit()
    return car


def create_engine(
    engine_name: str,
    base_price: int,
    session: Session,
) -> Engine:
    engine = Engine(
        engine_name=engine_name,
        base_price=base_price,
    )
    session.add(engine)
    session.commit()
    return engine


def create_salonemember(
    salone_name: str,
    base_price: int,
    session: Session,
) -> SaloneMember:
    salone_member = SaloneMember(
        salone_name=salone_name,
        base_price=base_price,
    )

    session.add(salone_member)
    session.commit()
    return salone_member


def create_saloneoption(
    salone_option_name: str,
    base_price: int,
    session: Session,
) -> SaloneOption:
    salone_option = SaloneOption(
        salone_option_name=salone_option_name,
        base_price=base_price,
    )

    session.add(salone_option)
    session.commit()
    return salone_option


def create_service(
    service_name: str,
    base_price: int,
    session: Session,
) -> Service:
    service = Service(
        service_name=service_name,
        base_price=base_price,
    )

    session.add(service)
    session.commit()
    return service


def create_shassi(
    shassi_name: str,
    base_price: int,
    session: Session,
) -> Shassi:
    shassi = Shassi(
        shassi_name=shassi_name,
        base_price=base_price,
    )
    session.add(shassi)
    session.commit()
    return shassi


#
def create_zip(
    zip_name: str,
    base_price: int,
    session: Session,
) -> Zip:
    zip1 = Zip(
        zip_name=zip_name,
        base_price=base_price,
    )
    session.add(zip1)
    session.commit()
    return zip1


################################
async def main_relations(
    session: Session,
):
    engine_1 = create_engine("двигатель 1", 1500, session)
    engine_2 = create_engine("двигатель 2", 2500, session)

    salone_member1 = create_salonemember("16 мест", 1500, session)
    salone_member2 = create_salonemember("20 мест", 2200, session)

    salone_option1 = create_saloneoption("обогрев", 1500, session)
    salone_option2 = create_saloneoption("задняя камера", 2200, session)

    service1 = create_service("домкрат", 1500, session)
    service2 = create_service("инструменты", 3300, session)

    shassi1 = create_shassi("подкачка колес", 1500, session)
    shassi2 = create_shassi("колпаки на колеса", 3300, session)

    zip1 = create_zip("зип стандарт", 1500, session)
    zip2 = create_zip("зип дополнительный", 3300, session)

    car1 = create_car(
        car_name="К-8 Грузовой 4х2,5",
        base_price=1_500_000,
        engine=engine_1,
        salone_member=salone_member1,
        session=session,
    )
    car2 = create_car(
        car_name="К-2 Легковой 5х2,5",
        base_price=2_999_000,
        engine=engine_2,
        salone_member=salone_member2,
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


    session.commit()


def get_car(session: Session) -> list[Car]:
    stmt = (
        select(Car)
        .options(
            selectinload(Car.),
        )
        .order_by(Car.id)
    )
    cars = session.scalars(stmt)
    return list(cars)


def demo_m2m(
    session: Session,
):
    main_relations(session)
    cars = get_car(session)
    for car in cars:
        print(car.login, car.hashed_password, "articles:")

