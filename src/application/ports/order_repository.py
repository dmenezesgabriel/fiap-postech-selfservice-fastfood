from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.entities.order import OrderDetail, OrderItem


class OrderRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create(self, order_detail: OrderDetail, ordem_items: List[OrderItem]) -> None:
        raise NotImplementedError

    # TODO
    # @abstractmethod
    # def list_all(self) -> List[Product]:
    #     raise NotImplementedError
