from abc import ABCMeta, abstractmethod
from typing import List

from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.entities.product import ProductEntity


class OrderRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create(
        self,
        order_detail: OrderDetailEntity,
        ordem_items: List[OrderItemEntity],
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[ProductEntity]:
        raise NotImplementedError
