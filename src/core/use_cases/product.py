from typing import List

from src.common.dto.product_dto import ProductDTO, ProductResponseDTO
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.core.domain.entities.product import ProductEntity
from src.core.domain.exceptions import EntityAlreadyExistsError, NotFoundError
from src.external.database.sqlalchemy.mappers.product_mapper import (
    ProductMapper,
)


class ProductService:
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create(self, product: ProductDTO) -> ProductEntity:

        existing_product: ProductEntity = (
            self.product_repository.get_by_product_name(
                product_name=product.name
            )
        )

        if existing_product:
            raise EntityAlreadyExistsError(
                f"Product with this name ({product.name}) already exists"
            )

        return self.product_repository.create(product)

    def update(self, product: ProductEntity) -> ProductEntity:
        existing_product = self.product_repository.get_by_id(product.id)

        if not existing_product:
            raise NotFoundError(f"Product with ID {product.id} not found")

        return self.product_repository.update(product)

    def get_by_id(self, product_id: int) -> ProductResponseDTO:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise NotFoundError(f"Product with ID {product_id} not found")

        return ProductMapper.entity_to_dto(product)

    def list_all(self) -> List[ProductResponseDTO]:
        products = self.product_repository.list_all()
        product_list = list()

        for product in products:
            product_list.append(
                ProductResponseDTO(
                    id=product.id,
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    category=product.category.name,
                    quantity=product.quantity,
                )
            )
        return product_list

    def list_by_category(self, category: str) -> List[ProductResponseDTO]:
        products = self.product_repository.list_by_category(category)
        product_list = list()

        for product in products:
            product_list.append(ProductMapper.entity_to_dto(product))
        return product_list

    def delete(self, product_id: int) -> bool:
        return self.product_repository.delete(product_id)
