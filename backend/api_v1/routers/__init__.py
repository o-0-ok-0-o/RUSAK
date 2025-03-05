from fastapi import APIRouter

from api_v1.routers.orders import router as order_router
from api_v1.routers.all import router as all_router

router = APIRouter(
    prefix="/api_v1/v1",
)

router.include_router(order_router)
router.include_router(all_router)
