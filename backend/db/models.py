from typing import Annotated, Optional

from fastapi import HTTPException, Query, APIRouter, Depends
from sqlmodel import Field, SQLModel, select

from db.database import SessionDep


class Order(SQLModel, table=True):
    """
    id: Уникальный идентификатор заказа
    order_date: Дата оформления заказа (строка в формате YYYY-MM-DD)
    customer_id: Идентификатор клиента, сделавшего заказ (внешний ключ, связан с таблицей Customer)
    total_amount: Общая сумма заказа
    status: Статус заказа (строка, enum: pending, processing, shipped, delivered, cancelled)
    shipping_address: Адрес
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    order_date: str = Field(index=True)  # YYYY-MM-DD
    customer_id: int
    total_amount: float
    status: str = Field(default="pending")  # pending, processing, done, cancelled
    shipping_address: str


router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@router.post("/", response_model=Order)
def create_hero(
    order: Annotated[Order, Depends()],
    session: SessionDep,
) -> Order:
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@router.get("/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Order]:
    orders = session.exec(select(Order).offset(offset).limit(limit)).all()
    return orders


@router.get("/{order_id}")
def read_hero(order_id: int, session: SessionDep) -> Order:
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.delete("/{order_id}")
def delete_hero(order_id: int, session: SessionDep):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    session.delete(order)
    session.commit()
    return {"ok": True}
