from abc import ABCMeta, abstractmethod
from typing import List

from src.application.dto.order_dto import OrderDTO, OrderResponseDTO
from src.infrastructure.database.sqlalchemy.repositories.order import (
    OrderRepository,
)


class OrderServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, order_repository: OrderRepository):
        raise NotImplementedError

    @abstractmethod
    def create(self, order_dto: OrderDTO) -> OrderResponseDTO:
        raise NotImplementedError
