from typing import List

from pydantic import BaseModel

from src.core.domain.value_objects.order_status import OrderStatus


class ProductDTO(BaseModel):
    id: int
    quantity: int

    model_config = {
        "json_schema_extra": {"examples": [{"id": 1, "quantity": 10}]}
    }


class CreateOrderDTO(BaseModel):
    user_id: int
    products: List[ProductDTO]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": 1,
                    "products": [
                        {"id": 1, "quantity": 10},
                        {"id": 2, "quantity": 10},
                    ],
                }
            ]
        }
    }


class CheckoutResponseDTO(BaseModel):
    id: int
    user_id: int
    transaction_amount: float
    payment_method: str
    description: str
    status: OrderStatus
    products: List[ProductDTO]


class OrderResponseDTO(BaseModel):
    id: int
    user_id: int
    total: float
    status: OrderStatus
    order_items: List[ProductDTO]
