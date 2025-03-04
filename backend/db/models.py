# from enum import Enum
# from utils.datetime import get_current_moscow_time
# from datetime import datetime
# from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
