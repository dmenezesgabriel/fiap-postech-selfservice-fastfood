from typing import List

from src.common.interfaces.product_gateway import ProductGatewayInterface
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.core.domain.entities.product import ProductEntity


class ProductGateway(ProductGatewayInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create(self, product: ProductEntity) -> ProductEntity:
        return self.product_repository.create(product=product)

    def update(self, product: ProductEntity) -> ProductEntity:
        return self.product_repository.update(product=product)

    def list_by_category(self, category: str) -> List[ProductEntity]:
        return self.product_repository.list_by_category(category=category)

    def list_all(self) -> List[ProductEntity]:
        return self.product_repository.list_all()

    def delete(self, product_id: int) -> bool:
        self.product_repository.delete(product_id=product_id)

    def get_by_product_name(self, product_name: str) -> ProductEntity:
        return self.product_repository.get_by_product_name(
            product_name=product_name
        )

    def get_by_id(self, product_id: str) -> ProductEntity:
        return self.product_repository.get_by_id(product_id=product_id)

    def get_many_by_ids(self, product_ids: List[int]) -> List[ProductEntity]:
        return self.product_repository.get_many_by_ids(product_ids=product_ids)
