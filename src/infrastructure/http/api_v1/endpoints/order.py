from fastapi import APIRouter

from src.application.services.order import OrderService
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)
from src.infrastructure.http.dto.order_dto import OrderDTO, OrderResponseDTO

router = APIRouter(prefix="/order", tags=["order"])

order_repository = OrderRepository()
product_repository = ProductRepository()
order_service = OrderService(order_repository, product_repository)


@router.post("/fake_checkout", response_model=OrderResponseDTO)
async def fake_checkout(order: OrderDTO):
    return order_service.create(order)
