from abc import ABCMeta, abstractmethod

from src.application.dto.order_dto import CreateOrderDTO, OrderResponseDTO
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)


class OrderServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, order_repository: OrderRepository):
        raise NotImplementedError

    @abstractmethod
    def create(self, order_dto: CreateOrderDTO) -> OrderResponseDTO:
        raise NotImplementedError
