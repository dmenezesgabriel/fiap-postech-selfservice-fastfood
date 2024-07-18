import abc
from typing import List

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity


class OrderGatewayInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
        self,
        createOrderDTO: CreateOrderDTO
    ) -> OrderResponseDTO:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[OrderDetailEntity]:
        raise NotImplementedError


    @abc.abstractmethod
    def update_order_status(self, order_id: int, order_status: str) -> OrderDetailEntity:
        raise NotImplementedError
