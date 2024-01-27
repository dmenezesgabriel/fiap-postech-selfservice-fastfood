from typing import List, Union

from pydantic import BaseModel, ConfigDict, Field

from src.domain.entities.product import Product


class OrderItem(BaseModel):
    id: Union[int, None] = None
    order_detail_id: Union[int, None] = None
    product_id: int
    product: Union[Product, None] = None


class OrderDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    order_items: List[OrderItem] = Field(default_factory=list)
    user_id: int
    total: float
