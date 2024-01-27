from datetime import datetime
from typing import List

from src.application.ports.order_repository import OrderRepositoryInterface
from src.domain.entities.order import OrderDetail, OrderItem
from src.infrastructure.database.sqlalchemy.mappers.order_mapper import (
    OrderMapper,
)
from src.infrastructure.database.sqlalchemy.models.order import (
    OrderDetail as OrderDetailModel,
)
from src.infrastructure.database.sqlalchemy.models.order import (
    OrderItem as OrderItemModel,
)
from src.infrastructure.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager,
)


class OrderRepository(OrderRepositoryInterface):
    def __init__(self):
        self._work_manager = SQLAlchemyUnitOfWorkManager()

    def create(
        self, order_detail: OrderDetail, order_items: List[OrderItem]
    ) -> None:
        with self._work_manager.start() as session:
            order_detail: OrderDetailModel = OrderDetailModel(
                user_id=order_detail.user_id,
                total=order_detail.total,
                updated_at=datetime.now(),
            )

            session.add(order_detail)

            session.flush()

            order_id: int = order_detail.id

            order_items_models = [
                OrderItemModel(
                    order_id=order_id,
                    product_id=item.product_id,
                    updated_at=datetime.now(),
                )
                for item in order_items
            ]

            session.bulk_save_objects(order_items_models)

    def list_all(self) -> List[OrderDetail]:
        with self._work_manager.start() as session:
            orders = session.query(OrderDetailModel).join(OrderItemModel).all()
            return [OrderMapper.model_to_entity(order) for order in orders]
