from typing import List

from fastapi import APIRouter, HTTPException

from src.common.dto.product_dto import ProductDTO, ProductResponseDTO
from src.communication.controller.product import ProductController
from src.external.database.sqlalchemy.repositories.product import (
    ProductRepository,
)

router = APIRouter(prefix="/products", tags=["products"])


product_repository = ProductRepository()
product_controller = ProductController(product_repository)


@router.post("/", response_model=ProductResponseDTO)
async def create_product(product: ProductDTO):
    return product_controller.create_product(product)


@router.get("/", response_model=List[ProductResponseDTO])
async def list_products():
    return product_controller.list_products()


@router.put("/{product_id}", response_model=ProductResponseDTO)
async def update_product(product_id: int, updated_product: ProductDTO):
    return product_controller.update_product(product_id, updated_product)


@router.get("/{category}", response_model=List[ProductResponseDTO])
async def list_by_category(category: str):
    return product_controller.list_products_by_category(category.title())


@router.delete("/{product_id}", response_model=str)
async def delete_product(product_id: int):

    if product_controller.get_product_by_id(product_id) is False:
        raise HTTPException(status_code=404, detail="Product not found")
    product_controller.delete_product(product_id)
    return "Product successfully removed"
