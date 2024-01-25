from decimal import Decimal
from typing import Union, List

from pydantic import ConfigDict, BaseModel
from datetime import datetime


class OrderItem(BaseModel):
    id: Union[int, None] = None
    order_detail_id: Union[int, None] = None
    product_id: int


class OrderDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    user_id: int
    total: float
