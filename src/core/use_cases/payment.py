from typing import List

from src.common.dto.payment_dto import CreatePaymentDTO
from src.common.interfaces.payment_gateway import PaymentGatewayInterface
from src.core.domain.entities.payment import PaymentEntity


class PaymentUseCase:
    @staticmethod
    def get_many_by_user_id(
        user_id: int, payment_gateway: PaymentGatewayInterface
    ) -> List[PaymentEntity]:
        return payment_gateway.get_many_by_user_id(user_id=user_id)

    @staticmethod
    def get_by_id(
        payment_id: int, payment_gateway: PaymentGatewayInterface
    ) -> PaymentEntity:
        return payment_gateway.get_by_id(payment_id=payment_id)

    @staticmethod
    def get_by_order_id(
        order_id: int, payment_gateway: PaymentGatewayInterface
    ) -> PaymentEntity:
        return payment_gateway.get_by_order_id(order_id=order_id)

    @staticmethod
    def create(
        payment: CreatePaymentDTO, payment_gateway: PaymentGatewayInterface
    ):
        if payment_gateway.get_by_order_id(order_id=payment.order_id):
            raise Exception("Payment already exists")
        new_payment = PaymentEntity(**payment.model_dump())
        return payment_gateway.create(payment=new_payment)

    @staticmethod
    def update(
        payment: PaymentEntity, payment_gateway: PaymentGatewayInterface
    ) -> PaymentEntity:
        return payment_gateway.update(payment=payment)

    @staticmethod
    def delete(
        payment_id: int, payment_gateway: PaymentGatewayInterface
    ) -> bool:
        return payment_gateway.delete(payment_id=payment_id)
