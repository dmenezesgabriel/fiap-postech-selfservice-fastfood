from typing import List

from src.core.application.ports.product_repository import ProductRepositoryInterface
from src.core.application.ports.product_service import ProductServiceInterface
from src.core.domain.entities.product import Product


class ProductService(ProductServiceInterface):

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create(self, product: Product) -> Product:
        return self.product_repository.create(product)

    def update(self, product: Product) -> Product:
        return self.product_repository.update(product)

    def list_all(self) -> List[Product]:
        products = self.product_repository.list_all()
        product_list = list()

        for product in products:
            product_list.append(
                Product(
                    id=product.id,
                    name=product.name,
                    price=product.price,
                    category=product.category.name,
                    quantity=product.quantity
                )
            )
        return product_list

    def list_by_category(self, category: str) -> List[Product]:
        products = self.product_repository.list_by_category(category)
        product_list = list()

        for product in products:
            product_list.append(
                Product(
                    id=product.id,
                    name=product.name,
                    price=product.price,
                    category=product.category.name,
                    quantity=product.quantity
                )
            )
        return product_list

    def delete(self, product_id: int) -> bool:
        return self.product_repository.delete(product_id)
