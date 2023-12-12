from abc import ABCMeta, abstractmethod

from src.adapter.driven.infra.database.sqlalchemy.repositories.product import ProductRepository
from src.core.domain.entities.product import Product


class ProductServicePort(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, product_repository: ProductRepository):
        raise NotImplementedError

    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError
