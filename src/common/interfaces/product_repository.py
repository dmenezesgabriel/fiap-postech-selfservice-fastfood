from abc import ABCMeta, abstractmethod
from typing import List

from src.core.domain.entities.product import ProductEntity


class ProductRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create(self, product: ProductEntity) -> ProductEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: ProductEntity) -> ProductEntity:
        raise NotImplementedError

    @abstractmethod
    def list_by_category(self, category: str) -> List[ProductEntity]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[ProductEntity]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_product_name(self, product_name: str) -> ProductEntity:
        raise NotImplementedError
