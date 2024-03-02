from fastapi import APIRouter

from src.common.dto.order_dto import CheckoutResponseDTO, CreateOrderDTO
from src.communication.controller.order import OrderController
from src.external.database.sqlalchemy.repositories.order import OrderRepository
from src.external.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/orders", tags=["orders"])

order_repository = OrderRepository()
product_repository = ProductRepository()
order_controller = OrderController(
    order_repository=order_repository, product_repository=product_repository
)


@router.post("/fake_checkout", response_model=CheckoutResponseDTO)
async def fake_checkout(order: CreateOrderDTO):
    return order_controller.create_order(order)


@router.get("/")
async def list_orders():
    return order_controller.list_orders()
