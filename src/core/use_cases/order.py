from typing import List

from src.common.dto.order_dto import (
    CheckoutResponseDTO,
    CreateOrderDTO,
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
    ) -> CheckoutResponseDTO:
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
        return CheckoutResponseDTO(
            id=new_order.id,
            user_id=new_order.user_id,
            transaction_amount=round(total, 2),
            payment_method="credit-card",
            description="Fake description",
            status=new_order.status,
            products=[
                ProductDTO(id=product.id, quantity=product.quantity)
                for product in new_order.order_items
            ],
        )

    @staticmethod
    def list_all(
            order_gateway: OrderGatewayInterface,
    ) -> List[OrderDetailEntity]:
        return order_gateway.list_all()

    @staticmethod
    def order_status_update(
            order_gateway: OrderGatewayInterface,
            order_id: int,
            order_status
    ) -> OrderDetailEntity:
        return order_gateway.update_order_status(order_id, order_status)
