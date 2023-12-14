from typing import List

from src.core.application.ports.product_repository import ProductRepositoryInterface
from src.core.application.ports.product_service import ProductServicePort
from src.core.domain.entities.product import Product


class ProductService(ProductServicePort):

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create(self, product: Product) -> Product:
        return self.product_repository.create(product)

    def update(self, product: Product) -> Product:
        return self.product_repository.update(product)

    def list_by_category(self, category: str) -> List[Product]:
        return self.product_repository.list_by_category(category)

    def delete(self, product: Product) -> bool:
        return self.product_repository.delete(product)
