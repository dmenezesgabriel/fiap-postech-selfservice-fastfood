from typing import Union

from pydantic import BaseModel, ConfigDict


class OrderItem(BaseModel):
    id: Union[int, None] = None
    order_detail_id: Union[int, None] = None
    product_id: int


class OrderDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    user_id: int
    total: float
