from typing import List

from src.common.dto.order_dto import (
    CreateOrderDTO,
    OrderResponseDTO,
    ProductDTO,
)
from src.common.interfaces.order_gateway import OrderGatewayInterface
from src.common.interfaces.product_gateway import ProductGatewayInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.value_objects.order_status import OrderStatus


class OrderUseCase:
    @staticmethod
    def create(
        order: CreateOrderDTO,
        order_gateway: OrderGatewayInterface,
        product_gateway: ProductGatewayInterface,
    ) -> OrderResponseDTO:
        total: float = 0

        product_ids = [order_product.id for order_product in order.products]
        products = product_gateway.get_many_by_ids(product_ids)

        for product, order_product in zip(products, order.products):
            total += product.price * order_product.quantity

        order_detail: OrderDetailEntity = OrderDetailEntity(
            user_id=order.user_id, total=total, status=OrderStatus.RECEIVED
        )

        order_items: List[OrderItemEntity] = [
            OrderItemEntity(product_id=item.id, quantity=item.quantity)
            for item in order.products
        ]

        new_order = order_gateway.create(order_detail, order_items)
        if not new_order.id:
            raise Exception("Error creating order")

        return OrderResponseDTO(
            id=new_order.id,
            user_id=new_order.user_id,
            total=round(total, 2),
            status=new_order.status,
            order_items=[
                ProductDTO(id=product.id, quantity=product.quantity)
                for product in new_order.order_items
                if product.id
            ],
        )

    @staticmethod
    def list_all(
        order_gateway: OrderGatewayInterface,
    ) -> List[OrderDetailEntity]:
        return order_gateway.list_all()
