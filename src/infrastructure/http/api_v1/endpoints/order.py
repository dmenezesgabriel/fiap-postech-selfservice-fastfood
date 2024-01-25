from fastapi import APIRouter

from src.application.services.order import OrderService
from src.infrastructure.database.sqlalchemy.repositories.order import OrderRepository

from src.infrastructure.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager,
)
from src.infrastructure.http.dto.order_dto import OrderDTO, OrderResponseDTO

router = APIRouter(prefix="/order", tags=["order"])

work_manager = SQLAlchemyUnitOfWorkManager()
order_repository = OrderRepository(work_manager)
order_service = OrderService(order_repository)


@router.post("/fake_checkout", response_model=OrderResponseDTO)
async def fake_checkout(order: OrderDTO):
    return order_service.create(order)
