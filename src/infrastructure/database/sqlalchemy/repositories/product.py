from typing import List

from src.application.ports.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.infrastructure.database.sqlalchemy.models.product import (
    Product as ProductModel,
)
from src.infrastructure.database.sqlalchemy.models.product import (
    ProductCategory,
)


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, work_manager):
        self._work_manager = work_manager

    def create(self, product: Product):
        with self._work_manager.start() as session:
            produto = ProductModel(
                name=product.name,
                category_id=product.category,
                price=product.price,
                quantity=product.quantity,
            )
            session.add(produto)
        return product

    def update(self, product: Product) -> Product:
        with self._work_manager.start as session:
            session.add(product)
        return product

    def list_by_category(self, category: str) -> List[Product]:
        with self._work_manager.start() as session:
            return (
                session.query(ProductModel)
                .join(ProductCategory)
                .filter(ProductCategory.name == category)
                .all()
            )

    def list_all(self) -> List[Product]:
        with self._work_manager.start() as session:
            products = session.query(ProductModel).join(ProductCategory).all()

            return products

    def delete(self, product_id: int) -> bool:
        with self._work_manager.start() as session:
            product = (
                session.query(ProductModel).filter_by(id=product_id).first()
            )
            if product is None:
                return False
            session.delete(product)
            return True
