from typing import Union

from pydantic import BaseModel

from src.core.domain.enum.payment import PaymentStatusEnum


class CreatePaymentDTO(BaseModel):
    # id: Union[int, None] = None
    order_id: Union[int, None] = None
    amount: float
    provider: str
    status: PaymentStatusEnum
    user_id: int = 1


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "order_id": 1,
                    "amount": 100.0,
                    "provider": "Stripe",
                    "status": "PENDING", ## TODO: remover status e deixar padrão "pending" no  microserviço de pagamentos
                }
            ]
        }
    }


class UpdatePaymentDTO(BaseModel):
    order_id: Union[int, None] = None
    user_id: Union[int, None] = None
    qr_data: Union[str, None] = None
    amount: float
    provider: str
    status: PaymentStatusEnum

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "order_id": 1,
                    "user_id": 1,
                    "amount": 100.0,
                    "provider": "Stripe",
                    "status": "PENDING",
                }
            ]
        }
    }


class PaymentDTO(BaseModel):
    id: int
    order_id: Union[int, None] = None
    user_id: Union[int, None] = None
    qr_data: Union[str, None] = None
    amount: float
    provider: str
    status: PaymentStatusEnum

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "order_id": 1,
                    "user_id": 1,
                    "amount": 100.0,
                    "provider": "Stripe",
                    "status": "PENDING",
                }
            ]
        }
    }


class WebhookDTO(BaseModel):
    order_id: int
    payment_status: PaymentStatusEnum

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "order_id": 1,
                    "payment_status": "CAPTURED",
                },
                {
                    "order_id": 1,
                    "payment_status": "DECLINED",
                },
            ]
        }
    }
