from typing import Union

from pydantic import BaseModel, ConfigDict

from src.core.domain.enum.payment import PaymentStatusEnum


class PaymentEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    qr_data: Union[str, None] = None
    order_id: int
    user_id: int
    amount: float
    provider: str
    status: PaymentStatusEnum
