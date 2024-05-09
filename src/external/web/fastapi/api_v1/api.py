from fastapi import APIRouter

from src.external.web.fastapi.api_v1.endpoints import (
    order,
    payment,
    products,
    users,
    auth
)

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


router.include_router(users.router)
router.include_router(products.router)
router.include_router(order.router)
router.include_router(payment.router)
router.include_router(auth.router)
