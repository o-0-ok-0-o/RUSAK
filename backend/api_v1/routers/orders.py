from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends, Form
from sqlmodel import select

from api_v1.crud.order import create_order_crud
from api_v1.schemas.order import OrderBaseSchema, OrderCreateSchema, OrderSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_async_session
from db.models import Order

router = APIRouter(
    prefix="/send-order-email",
    tags=["Заказы"],
)


@router.post("/submit")
async def create_order(
    order: Annotated[OrderCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
    # customer:str = Form(),
    # phone: str = Form(),
    # email: str = Form(),
):
    await create_order_crud(
        order=order,
        session=session,
    )
    return order


@router.get("", response_model=list[OrderBaseSchema])
async def read_orders(
    session: AsyncSession = Depends(get_async_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    orders = await session.scalars(select(Order).offset(offset).limit(limit))
    return orders


@router.get("/{order_id}", response_model=OrderBaseSchema)
async def read_order(
    order_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    order = await session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.delete("/{order_id}")
async def delete_order(
    order_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    order = await session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    await session.delete(order)
    await session.commit()
    return {"deleted": "success"}
