from datetime import datetime
from typing import List

from src.application.ports.order_repository import OrderRepositoryInterface
from src.domain.entities.order import OrderDetail, OrderItem
from src.infrastructure.database.sqlalchemy.models.order import OrderDetail as OrderDetailModel
from src.infrastructure.database.sqlalchemy.models.order import OrderItem as OrderItemModel


class OrderRepository(OrderRepositoryInterface):
    def __init__(self, work_manager):
        self._work_manager = work_manager

    def create(self, order_detail: OrderDetail, ordem_items: List[OrderItem]) -> None:
        with self._work_manager.start() as session:
            order_detail: OrderDetailModel = OrderDetailModel(
                user_id=order_detail.user_id,
                total=order_detail.total,
                updated_at=datetime.now()
            )

            session.add(order_detail)

            session.flush()

            order_id: int = order_detail.id

            for item in ordem_items:
                session.add(
                    OrderItemModel(
                        order_id=order_id,
                        product_id=item.product_id,
                        updated_at=datetime.now()
                    )
                )
