from typing import List

from src.common.interfaces.payment_gateway import PaymentGatewayInterface
from src.common.interfaces.payment_repository import PaymentRepositoryInterface
from src.core.domain.entities.payment import PaymentEntity


class PaymentGateway(PaymentGatewayInterface):
    def __init__(self, payment_repository: PaymentRepositoryInterface) -> None:
        self.payment_repository = payment_repository

    def get_many_by_user_id(self, user_id: int) -> List[PaymentEntity]:
        return self.payment_repository.get_many_by_user_id(user_id=user_id)

    def get_by_id(self, payment_id: int) -> PaymentEntity:
        return self.payment_repository.get_by_id(payment_id=payment_id)

    def get_by_order_id(self, order_id: int) -> PaymentEntity:
        return self.payment_repository.get_by_order_id(order_id=order_id)

    def create(self, payment: PaymentEntity) -> PaymentEntity:
        return self.payment_repository.create(payment=payment)

    def update(self, payment: PaymentEntity) -> PaymentEntity:
        return self.payment_repository.update(payment=payment)

    def delete(self, payment_id: int) -> None:
        return self.payment_repository.delete(payment_id=payment_id)
