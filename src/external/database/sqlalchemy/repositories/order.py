from datetime import datetime
from typing import List

from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.external.database.sqlalchemy.mappers.order_mapper import OrderMapper
from src.external.database.sqlalchemy.models.order import (
    OrderDetailModel,
    OrderItemModel,
)
from src.external.database.sqlalchemy.session_mixin import use_database_session


class OrderRepository(OrderRepositoryInterface):

    def create(
        self,
        order_detail: OrderDetailEntity,
        order_items: List[OrderItemEntity],
    ) -> OrderDetailEntity:
        with use_database_session() as session:
            order_detail_model = OrderDetailModel(
                user_id=order_detail.user_id,
                total=order_detail.total,
                updated_at=datetime.now(),
                status=str(order_detail.status),
            )

            session.add(order_detail_model)

            session.flush()

            order_id: int = order_detail_model.id

            order_items_models = [
                OrderItemModel(
                    order_id=order_id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    updated_at=datetime.now(),
                )
                for item in order_items
            ]

            session.bulk_save_objects(order_items_models)
            session.commit()
            return OrderMapper.model_to_entity(order_detail_model)

    def list_all(self) -> List[OrderDetailEntity]:
        with use_database_session() as session:
            orders = session.query(OrderDetailModel).join(OrderItemModel).all()
            return [OrderMapper.model_to_entity(order) for order in orders]
