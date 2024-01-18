from typing import List

from fastapi import APIRouter

from src.adapter.driven.infra.database.sqlalchemy.repositories.product import ProductRepository
from src.adapter.driven.infra.database.sqlalchemy.unit_of_work_manager import SQLAlchemyUnitOfWorkManager
from src.core.application.services.product import ProductService
from src.core.domain.entities.product import Product

router = APIRouter(prefix="/products", tags=["products"])

work_manager = SQLAlchemyUnitOfWorkManager()
product_repository = ProductRepository(work_manager)
product_service = ProductService(product_repository)


@router.post("/", response_model=Product)
async def create_product(product: Product):
    return product_service.create(product)


@router.get("/", response_model=List[Product])
async def list_product():
    return product_service.list_all()


@router.get("/{category}", response_model=List[Product])
async def list_by_category(category: str):
    return product_service.list_by_category(category.title())


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return product_service.delete(product_id)