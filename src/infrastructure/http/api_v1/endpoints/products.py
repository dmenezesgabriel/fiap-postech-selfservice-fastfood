from typing import List

from fastapi import APIRouter, HTTPException

from src.application.dto.product_dto import ProductDTO, ProductResponseDTO
from src.application.services.product import ProductService
from src.domain.entities.product import Product
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/products", tags=["products"])


product_repository = ProductRepository()
product_service = ProductService(product_repository)


@router.post("/", response_model=ProductResponseDTO)
async def create_product(product: ProductDTO):
    """
     # Criação de produto

     ## Observações:

     * O campo name deve ser único na base de dados
     """
    return product_service.create(product)


@router.get("/", response_model=List[ProductResponseDTO])
async def list_product():
    return product_service.list_all()


@router.put("/{product_id}", response_model=ProductResponseDTO)
async def update_product(product_id: int, updated_product: ProductDTO):
    product = Product(id=product_id, **updated_product.model_dump())
    return product_service.update(product)


@router.get("/{category}", response_model=List[ProductResponseDTO])
async def list_by_category(category: str):
    """
         # Busca por categoria

         ## Observações:

         * ex: lanche, sobremesa, bebida, acompanhamento"""
    return product_service.list_by_category(category.title())


@router.delete("/{product_id}", response_model=str)
async def delete_product(product_id: int):

    if product_service.get_by_id(product_id) is False:
        raise HTTPException(status_code=404, detail="Product not found")
    product_service.delete(product_id)
    return "Product successfully removed"


