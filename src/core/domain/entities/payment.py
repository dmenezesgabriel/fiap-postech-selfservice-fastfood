from typing import Union

from pydantic import BaseModel, ConfigDict

from src.core.domain.enum.payment import PaymentStatusEnum


class PaymentEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    order_id: int
    amount: float
    provider: str
    status: PaymentStatusEnum
