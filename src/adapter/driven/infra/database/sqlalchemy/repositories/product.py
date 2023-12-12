from src.core.application.ports.product_repository import ProductRepositoryPort
from src.core.domain.entities.product import Product


class ProductRepository(ProductRepositoryPort):

    def __init__(self, work_manager):
        self._work_manager = work_manager

    def create(self, product: Product):
        with self._work_manager.start() as session:
            session.add(product)
        return product
