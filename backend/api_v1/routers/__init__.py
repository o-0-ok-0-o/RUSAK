from fastapi import APIRouter

from api_v1.routers.orders import router as order_router

router = APIRouter(
    prefix="/api_v1/v1",
)

router.include_router(router)
