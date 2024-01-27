from datetime import datetime
from typing import List

from src.application.dto.order_dto import (
    CheckoutResponseDTO,
    OrderDTO,
    OrderResponseDTO,
)
from src.application.ports.order_service import OrderServiceInterface
from src.domain.entities.order import OrderDetail, OrderItem
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)


class OrderService(OrderServiceInterface):
    def __init__(
        self,
        order_repository: OrderRepository,
        product_repository: ProductRepository,
    ):
        self.order_repository = order_repository
        self.product_repository = product_repository

    def create(self, order: OrderDTO) -> OrderResponseDTO:
        total: float = 0

        product_ids = [order_product.id for order_product in order.products]
        products = self.product_repository.get_many_by_ids(product_ids)

        for product, order_product in zip(products, order.products):
            total += product.price * order_product.quantity

        order_detail: OrderDetail = OrderDetail(
            user_id=order.user_id,
            total=total,
        )

        order_items: List[OrderItem] = [
            OrderItem(product_id=item.id) for item in order.products
        ]

        self.order_repository.create(order_detail, order_items)

        return CheckoutResponseDTO(
            user_id=order.user_id,
            transacion_amount=round(total, 2),
            payment_method="credit-card",
            description="Fake description",
            products=order.products,
        )

    def list_all(self) -> List[OrderDetail]:
        return self.order_repository.list_all()
