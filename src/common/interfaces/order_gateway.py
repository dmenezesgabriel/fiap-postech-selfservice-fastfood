import abc
from typing import List

from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.entities.product import ProductEntity


class OrderGatewayInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
        self,
        order_detail: OrderDetailEntity,
        order_items: List[OrderItemEntity],
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[ProductEntity]:
        raise NotImplementedError
