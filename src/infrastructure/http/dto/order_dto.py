from typing import List, Union

from pydantic import BaseModel, ConfigDict, EmailStr, validator


class ProductDTO(BaseModel):
    id: int
    quantity: int

    model_config = {
        "json_schema_extra": {"examples": [{"id": 1, "quantity": 10}]}
    }


class OrderDTO(BaseModel):
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
    user_id: int
    transacion_amount: float
    payment_method: str
    description: str
    products: List[ProductDTO]


class OrderResponseDTO(BaseModel):
    user_id: int
    total: float
    order_items: List[ProductDTO]
