from src.core.application.ports.product_repository import ProductRepositoryPort
from src.core.application.ports.product_service import ProductServicePort
from src.core.domain.entities.product import Product


class ProductService(ProductServicePort):
    def __init__(self, product_repository: ProductRepositoryPort):
        self.product_repository = product_repository

    def create(self, product: Product) -> Product:
        return self.product_repository.create(product)
