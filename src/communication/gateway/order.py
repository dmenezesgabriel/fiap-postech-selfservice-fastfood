from typing import List

from src.common.interfaces.order_gateway import OrderGatewayInterface
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.entities.product import ProductEntity


class OrderGateway(OrderGatewayInterface):
    def __init__(self, order_repository: OrderRepositoryInterface):
        self.order_repository = order_repository

    def create(
        self,
        order_detail: OrderDetailEntity,
        order_items: List[OrderItemEntity],
    ):
        return self.order_repository.create(
            order_detail=order_detail, order_items=order_items
        )

    def list_all(self) -> List[ProductEntity]:
        return self.order_repository.list_all()

    def update_order_status(self, order_id: int, order_status: str):
        return self.order_repository.update_order_status(order_id, order_status)
