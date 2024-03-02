from fastapi import APIRouter

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO
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


@router.post("/", response_model=OrderResponseDTO)
async def create_order(order: CreateOrderDTO):
    return order_controller.create_order(order)


@router.get("/")
async def list_orders():
    return order_controller.list_orders()
