from typing import List

from src.application.dto.product_dto import ProductDTO
from src.application.ports.product_repository import ProductRepositoryInterface
from src.domain.base.exceptions import EntityAlreadyExistsError, NotFoundError
from src.domain.entities.product import Product


class ProductService:
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create(self, product: ProductDTO) -> Product:

        existing_product : Product = self.product_repository.get_by_name(name=product.name)

        if existing_product:
            raise EntityAlreadyExistsError(f"Product with this name ({product.name}) already exists")

        return self.product_repository.create(product)

    def update(self, product: Product) -> Product:
        existing_product = self.product_repository.get_by_id(product.id)

        if not existing_product:
            raise NotFoundError(f"Product with ID {product.id} not found")

        return self.product_repository.update(product)

    def get_by_id(self, product_id: int) -> Product:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise NotFoundError(f"Product with ID {product_id} not found")

        return Product(
            id=product.id,
            name=product.name,
            price=product.price,
            category=product.category.name,
            quantity=product.quantity,
        )

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
                    quantity=product.quantity,
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
                    quantity=product.quantity,
                )
            )
        return product_list

    def delete(self, product_id: int) -> bool:
        return self.product_repository.delete(product_id)
