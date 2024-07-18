from typing import List

from src.common.dto.order_dto import (
    CreateOrderDTO,
    OrderResponseDTO,
    ProductDTO,
)
from src.common.interfaces.order_gateway import OrderGatewayInterface
from src.common.interfaces.product_gateway import ProductGatewayInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.entities.product import ProductEntity
from src.core.domain.value_objects.order_status import OrderStatus


class OrderUseCase:
    @staticmethod
    def create(
            order_dto: CreateOrderDTO,
            order_gateway: OrderGatewayInterface,
            product_gateway: ProductGatewayInterface,
    ) -> OrderResponseDTO:
        total: float = 0

        product_ids = [order_product.sku for order_product in order_dto.products]
        products = product_gateway.get_many_by_ids(product_ids)

        for product, order_product in zip(products, order_dto.products):
            total += product.price * order_product.quantity

        # order_detail: OrderDetailEntity = OrderDetailEntity(
        #     total=total, status=OrderStatus.RECEIVED
        # )
        #
        # order_items: List[OrderItemEntity] = [
        #     OrderItemEntity(product_id=item.id, quantity=item.quantity)
        #     for item in order_dto.products
        # ]

        new_order: OrderResponseDTO = order_gateway.create(order_dto)
        if not new_order.id:
            raise Exception("Error creating order")

        return OrderResponseDTO(
            id=new_order.id,
            created_at=new_order.created_at,
            status=new_order.status,
            order_items=[
                OrderItemEntity(id=product.id, quantity=product.quantity, product=product.product)
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
