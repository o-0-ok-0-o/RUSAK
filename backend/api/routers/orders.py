from typing import Annotated

from fastapi import HTTPException, Query, APIRouter, Depends
from sqlmodel import select, Session

from api.schemas.schemas import OrderBaseSchema, OrderSchema, OrderCreateSchema
from db.database import SessionDep, get_session
from db.models import Order

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@router.post("/")
def create_order(
    order: Annotated[OrderCreateSchema, Depends()],
    session: Session = Depends(get_session),
):
    order_dict = order.model_dump()
    order_model = Order(**order_dict)
    session.add(order_model)
    session.commit()
    return order


@router.get("/", response_model=list[OrderBaseSchema])
def read_order(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    orders = session.exec(select(Order).offset(offset).limit(limit)).all()
    return orders


@router.get("/{order_id}", response_model=OrderBaseSchema)
def read_order(order_id: int, session: SessionDep):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.delete("/{order_id}")
def delete_order(order_id: int, session: SessionDep):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    session.delete(order)
    session.commit()
    return {"ok": True}
