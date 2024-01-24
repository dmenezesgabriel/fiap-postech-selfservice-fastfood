from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.entities.product import Product
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)


class ProductServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, product_repository: ProductRepository):
        raise NotImplementedError

    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def list_by_category(self, category: str) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        raise NotImplementedError
