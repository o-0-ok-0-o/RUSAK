from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends

# from db.database import SessionDep, get_session


router = APIRouter(
    prefix="/salone-member",
    tags=["Салон кол-во"],
)
