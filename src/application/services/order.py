from datetime import datetime
from typing import List

from src.application.ports.order_service import OrderServiceInterface
from src.domain.entities.order import OrderDetail, OrderItem
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)
from src.infrastructure.http.dto.order_dto import OrderDTO, OrderResponseDTO


class OrderService(OrderServiceInterface):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create(self, order: OrderDTO) -> OrderResponseDTO:
        total: float = 0

        for product in order.products:
            total += product.price * product.quantity

        order_detail: OrderDetail = OrderDetail(
            user_id=order.user_id, total=total, updated_at=datetime.now()
        )

        order_items: List[OrderItem] = [
            OrderItem(product_id=item.id) for item in order.products
        ]

        self.order_repository.create(order_detail, order_items)

        return OrderResponseDTO(
            user_id=order.user_id,
            transacion_amount=round(total, 2),
            payment_method="credit-card",
            description="Fake description",
            products=order.products,
        )
