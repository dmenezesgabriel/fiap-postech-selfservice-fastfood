from src.domain.entities.order import OrderDetail as OrderDetailEntity
from src.domain.entities.order import OrderItem as OrderItemEntity
from src.domain.entities.product import Product as ProductEntity
from src.infrastructure.database.sqlalchemy.models.order import (
    OrderDetail as OrderDetailModel,
)
from src.infrastructure.database.sqlalchemy.models.order import (
    OrderItem as OrderItemModel,
)


class OrderMapper:
    @staticmethod
    def model_to_entity(order_detail_model):
        order_items = [
            OrderItemEntity(
                id=item.id,
                order_detail_id=order_detail_model.id,
                product_id=item.product_id,
                product=ProductEntity(
                    id=item.product.id,
                    name=item.product.name,
                    category=item.product.category.name,
                    price=item.product.price,
                    quantity=item.product.quantity,
                ),
            )
            for item in order_detail_model.order_items
        ]

        return OrderDetailEntity(
            id=order_detail_model.id,
            order_items=order_items,
            user_id=order_detail_model.user_id,
            total=order_detail_model.total,
        )

    @staticmethod
    def entity_to_model(order_detail_entity):
        order_items_models = [
            OrderItemModel(
                order_id=order_detail_entity.id, product_id=item.product_id
            )
            for item in order_detail_entity.order_items
        ]

        return OrderDetailModel(
            id=order_detail_entity.id,
            user_id=order_detail_entity.user_id,
            total=order_detail_entity.total,
            order_items=order_items_models,
        )
