from typing import List

from fastapi import APIRouter

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO, OrderStatusDTO
from src.communication.controller.order import OrderController
from src.external.database.sqlalchemy.repositories.order import OrderRepository
from src.external.database.sqlalchemy.repositories.payment import PaymentRepository
from src.external.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/orders", tags=["orders"])

order_repository = OrderRepository()
product_repository = ProductRepository()
payment_repository = PaymentRepository()
order_controller = OrderController(
    order_repository=order_repository, product_repository=product_repository, payment_repository=payment_repository
)


@router.post("/", response_model=OrderResponseDTO, response_model_exclude_none=True)
async def create_order(order: CreateOrderDTO):
    return order_controller.create_order(order)
