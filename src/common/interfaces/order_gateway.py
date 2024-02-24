import abc
from typing import List

from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity


class OrderGatewayInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
        self,
        order_detail: OrderDetailEntity,
        order_items: List[OrderItemEntity],
    ) -> OrderDetailEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[OrderDetailEntity]:
        raise NotImplementedError
