from abc import ABCMeta, abstractmethod
from typing import List

from src.adapter.driven.infra.database.sqlalchemy.repositories.product import ProductRepository
from src.core.domain.entities.product import Product


class ProductServicePort(metaclass=ABCMeta):
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
    def delete(self, product: Product) -> bool:
        raise NotImplementedError