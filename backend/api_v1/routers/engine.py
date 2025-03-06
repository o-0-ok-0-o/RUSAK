from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends
from sqlmodel import select, Session
from api_v1.schemas.schemas import OrderBaseSchema, OrderSchema, OrderCreateSchema

# from db.database import SessionDep, get_session
from db.models import Order


router = APIRouter(
    prefix="/engines",
    tags=["Двигатели"],
)
