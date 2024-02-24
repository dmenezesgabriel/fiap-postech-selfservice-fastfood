from src.common.dto.product_dto import ProductDTO
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.communication.gateway.product import ProductGateway
from src.core.domain.entities.product import ProductEntity
from src.core.use_cases.product import ProductUseCase


class ProductController:
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create_product(self, product: ProductDTO):
        product_gateway = ProductGateway(self.product_repository)
        return ProductUseCase.create(
            product=product, product_gateway=product_gateway
        )

    def list_products(self):
        product_gateway = ProductGateway(self.product_repository)
        return ProductUseCase.list_all(product_gateway=product_gateway)

    def update_product(self, product_id: int, updated_product: ProductDTO):
        product_gateway = ProductGateway(self.product_repository)
        product = ProductEntity(id=product_id, **updated_product.model_dump())
        return ProductUseCase.update(
            product=product, product_gateway=product_gateway
        )

    def list_products_by_category(self, category: str):
        product_gateway = ProductGateway(self.product_repository)
        return ProductUseCase.list_by_category(
            category=category, product_gateway=product_gateway
        )

    def get_product_by_id(self, product_id: int):
        product_gateway = ProductGateway(self.product_repository)
        return ProductUseCase.get_by_id(
            product_id=product_id, product_gateway=product_gateway
        )

    def delete_product(self, product_id: int):
        product_gateway = ProductGateway(self.product_repository)
        return ProductUseCase.delete(
            product_id=product_id, product_gateway=product_gateway
        )
