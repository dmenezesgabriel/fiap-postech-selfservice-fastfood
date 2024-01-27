from typing import List

from fastapi import APIRouter

from src.application.dto.order_dto import (
    CheckoutResponseDTO,
    OrderDTO,
    OrderResponseDTO,
)
from src.application.services.order import OrderService
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/order", tags=["order"])

order_repository = OrderRepository()
product_repository = ProductRepository()
order_service = OrderService(order_repository, product_repository)


@router.post("/fake_checkout", response_model=CheckoutResponseDTO)
async def fake_checkout(order: OrderDTO):
    return order_service.create(order)


@router.get("/")
async def list_orders():
    return order_service.list_all()
