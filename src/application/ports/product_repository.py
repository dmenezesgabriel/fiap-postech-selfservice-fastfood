from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.entities.product import Product


class ProductRepositoryInterface(metaclass=ABCMeta):
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

    @abstractmethod
    def get_by_product_name(self, product_name: str) -> Product:
        raise NotImplementedError
