from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends
from sqlmodel import select, Session
from api_v1.schemas.schemas import OrderBaseSchema, OrderSchema, OrderCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_async_session
from db.models import Order


router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@router.post("")
async def create_order(
    order: Annotated[OrderCreateSchema, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    order_dict = order.model_dump()
    order_model = Order(**order_dict)
    session.add(order_model)
    await session.commit()
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
