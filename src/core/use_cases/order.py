from typing import List

from src.common.dto.order_dto import (
    CreateOrderDTO,
    OrderResponseDTO,
    KitchenResponseDTO,
)
from src.common.dto.payment_dto import CreatePaymentDTO
from src.common.interfaces.order_gateway import OrderGatewayInterface
from src.common.interfaces.payment_gateway import PaymentGatewayInterface
from src.common.interfaces.product_gateway import ProductGatewayInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.enum.payment import PaymentStatusEnum


class OrderUseCase:
    @staticmethod
    def create(
            order_dto: CreateOrderDTO,
            order_gateway: OrderGatewayInterface,
            payment_gateway: PaymentGatewayInterface,
            product_gateway: ProductGatewayInterface,
    ) -> OrderResponseDTO:
        try:
            total: float = 0

            product_ids = [order_product.sku for order_product in order_dto.products]
            products = product_gateway.get_many_by_ids(product_ids)

            for product, order_product in zip(products, order_dto.products):
                total += product.price * order_product.quantity

            new_order: KitchenResponseDTO = order_gateway.create(order_dto)

            if not new_order.id:
                raise Exception("Error creating order")

            payment_response = payment_gateway.create(CreatePaymentDTO(order_id=new_order.id,
                                                                       amount=total,
                                                                       provider="STRIPE",
                                                                       status=PaymentStatusEnum.PENDING))

            if not payment_response:
                raise Exception("Error creating payment")

            return OrderResponseDTO(
                id=new_order.id,
                created_at=new_order.created_at,
                status=new_order.status,
                order_items=[
                    OrderItemEntity(quantity=new_order.order_items[idx].quantity, product=product)
                    for idx, product in enumerate(products)
                ],
                total=total
            )
        except Exception as error:
            print(error)

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
