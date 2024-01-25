from abc import ABCMeta, abstractmethod
from typing import List

from src.infrastructure.database.sqlalchemy.repositories.order import OrderRepository
from src.infrastructure.http.dto.order_dto import OrderDTO, OrderResponseDTO


class OrderServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, order_repository: OrderRepository):
        raise NotImplementedError

    @abstractmethod
    def create(self, order_dto: OrderDTO) -> OrderResponseDTO:
        raise NotImplementedError
