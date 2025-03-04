import re

from pydantic import BaseModel, EmailStr, Field, field_validator


# Заказы
class OrderBaseSchema(BaseModel):
    customer: str
    phone: str = Field(
        default=...,
        description="Номер телефона в международном формате, начинающийся с '+'",
    )
    email: EmailStr = Field(default=..., description="Электронная почта студента")

    @field_validator("phone", check_fields=False)
    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        if not re.match(r"^\+7\d{10}$", phone_number):
            raise ValueError(
                'Номер телефона должен начинаться с "+7" и содержать 11 цифр'
            )
        return phone_number


class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderSchema(OrderBaseSchema):
    id: int


# def test_valid_order(data: dict) -> None:
#     try:
#         student = OrderBaseSchema(**data)
#         print(student)
#     except ValidationError as e:
#         print(f"Ошибка валидации: {e}")
#
#
# order_data = {
#     "customer": "Pavlov",
#     "phone": "+79999999999",
#     "email": "ivan.ivanov@example.com",
# }
#
# test_valid_order(order_data)
