from typing import List

from src.adapter.driven.infra.database.sqlalchemy.models.product import Product, ProductCategory
from src.adapter.driver.api.controllers.product_route import ProductController
from src.core.application.ports.product_repository import ProductRepositoryInterface
from src.core.domain.entities.product import Product


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, work_manager):
        self._work_manager = work_manager

    def create(self, product: Product):
        with self._work_manager.start() as session:
            produto = Product(name='teste', category_id=ProductCategory(id=1), price=20, quantity=100)
            session.add(produto)
        return product


    def update(self, product: Product) -> Product:
        with self._work_manager.start as session:
            session.add(product)
        return product

    def list_by_category(self, category: str) -> List[Product]:
        with self._work_manager.start() as session:
            session.query(Product).join(ProductCategory).filter(ProductCategory.name == category).all()

    def delete(self, product_id: int) -> bool:
        pass
