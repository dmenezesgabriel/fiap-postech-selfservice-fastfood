from src.common.dto.product_dto import ProductResponseDTO
from src.core.domain.entities.product import ProductEntity


class ProductMapper:
    @staticmethod
    def entity_to_dto(product_entity: ProductEntity) -> ProductResponseDTO:
        return ProductResponseDTO(
            id=product_entity.id,
            name=product_entity.name,
            category=product_entity.category.name,
            description=product_entity.description,
            price=product_entity.price,
            quantity=product_entity.quantity,
        )
