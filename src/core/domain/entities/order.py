from typing import List, Union

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.product import ProductEntity


class OrderItemEntity(BaseModel):
    id: Union[int, None] = None
    order_detail_id: Union[int, None] = None
    product_id: int
    product: Union[ProductEntity, None] = None
    quantity: int


class OrderDetailEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    order_items: List[OrderItemEntity] = Field(default_factory=list)
    user_id: int
    total: float
