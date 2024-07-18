from src.common.dto.product_dto import ProductResponseDTO
from src.core.domain.entities.product import ProductEntity
from src.external.database.sqlalchemy.models.product import ProductModel


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

    @staticmethod
    def model_to_entity(product_model: ProductModel) -> ProductEntity:
        return ProductEntity(
            id=product_model.id,
            description=product_model.description,
            name=product_model.name,
        )
