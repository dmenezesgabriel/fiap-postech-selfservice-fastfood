from src.application.dto.product_dto import ProductResponseDTO
from src.domain.entities.product import Product


class ProductMapper:
    @staticmethod
    def entity_to_dto(product_entity: Product) -> ProductResponseDTO:
        return ProductResponseDTO(
            id=product_entity.id,
            name=product_entity.name,
            category=product_entity.category.name,
            description=product_entity.description,
            price=product_entity.price,
            quantity=product_entity.quantity,
        )
