from abc import ABCMeta, abstractmethod

from src.core.domain.entities.product import Product


class ProductRepositoryPort(metaclass=ABCMeta):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError
