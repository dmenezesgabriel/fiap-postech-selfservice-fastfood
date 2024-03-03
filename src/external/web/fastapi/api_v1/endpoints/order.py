from fastapi import APIRouter

from src.common.dto.order_dto import CheckoutResponseDTO, CreateOrderDTO, OrderStatusDTO
from src.communication.controller.order import OrderController
from src.external.database.sqlalchemy.repositories.order import OrderRepository
from src.external.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/order", tags=["order"])

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


@router.put("/{order_id}")
async def update_order_status(order_id: int, order_status: OrderStatusDTO):
    return order_controller.update_order_status(order_id, order_status.status.title())
