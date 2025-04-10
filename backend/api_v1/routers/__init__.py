from fastapi import APIRouter

from api_v1.routers.calculator import router as test_router
from api_v1.routers.orders import router as order_router
from api_v1.routers.engine import router as engine_router
from api_v1.routers.salone_member import router as salone_member_router
from api_v1.routers.salone_option import router as salone_option_router
from api_v1.routers.service import router as service_router
from api_v1.routers.shassi import router as shassi_router
from api_v1.routers.zip import router as zip_router
from api_v1.routers.tire import router as tire_router
from api_v1.routers.wheelbase import router as wheelbase_router
from api_v1.routers.photo import router as photo_router
from api_v1.routers.car import router as car_router

router = APIRouter(
    prefix="/api_v1",
)

router.include_router(test_router)
router.include_router(order_router)
router.include_router(engine_router)
router.include_router(salone_member_router)
router.include_router(salone_option_router)
router.include_router(zip_router)
router.include_router(service_router)
router.include_router(shassi_router)
router.include_router(tire_router)
router.include_router(wheelbase_router)
router.include_router(photo_router)
router.include_router(car_router)
