from fastapi import APIRouter

from src.common.dto.order_dto import CheckoutResponseDTO, CreateOrderDTO
from src.core.use_cases.order import OrderService
from src.external.database.sqlalchemy.repositories.order import OrderRepository
from src.external.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/order", tags=["order"])

order_repository = OrderRepository()
product_repository = ProductRepository()
order_service = OrderService(order_repository, product_repository)


@router.post("/fake_checkout", response_model=CheckoutResponseDTO)
async def fake_checkout(order: CreateOrderDTO):
    return order_service.create(order)


@router.get("/")
async def list_orders():
    return order_service.list_all()
