import abc
from typing import List

from src.common.dto.payment_dto import CreatePaymentDTO
from src.core.domain.entities.payment import PaymentEntity


class PaymentGatewayInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_many_by_user_id(self, user_id: int) -> List[PaymentEntity]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, payment_id: int) -> PaymentEntity:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_order_id(self, order_id: int) -> PaymentEntity:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, payment: CreatePaymentDTO) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, payment_id: int) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(payment: PaymentEntity) -> PaymentEntity:
        raise NotImplementedError()
