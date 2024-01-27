from typing import List

from fastapi import APIRouter

from src.application.dto.product_dto import ProductDTO, ProductDTOResponse
from src.application.services.product import ProductService
from src.domain.entities.product import Product
from src.infrastructure.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/products", tags=["products"])


product_repository = ProductRepository()
product_service = ProductService(product_repository)


@router.post("/", response_model=ProductDTOResponse)
async def create_product(product: ProductDTO):
    return product_service.create(product)


@router.get("/", response_model=List[ProductDTOResponse])
async def list_product():
    return product_service.list_all()


@router.put("/{product_id}", response_model=ProductDTOResponse)
async def update_product(product_id: int, updated_product: ProductDTO):
    product = Product(id=product_id, **updated_product.dict())
    return product_service.update(product)


@router.get("/{category}", response_model=List[ProductDTOResponse])
async def list_by_category(category: str):
    return product_service.list_by_category(category.title())


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return product_service.delete(product_id)
