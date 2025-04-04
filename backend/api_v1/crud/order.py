from api_v1.schemas.order import OrderCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Order
from utils.send_order_email import submit


async def create_order_crud(
    order: OrderCreateSchema,
    session: AsyncSession,
    # customer:str,
    # phone: str,
    # email: str,
):
    order_dict = order.model_dump()
    await submit(
        customer=order_dict["customer"],
        phone=order_dict["phone"],
        email=order_dict["email"],
    )
    order_model = Order(**order_dict)
    session.add(order_model)
    await session.commit()
    return order
