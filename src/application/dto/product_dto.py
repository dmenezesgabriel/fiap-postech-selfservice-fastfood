from decimal import Decimal
from typing import Union, Any

from pydantic import BaseModel


class ProductDTO(BaseModel):
    # id: Union[int, None] = None
    name: str
    category: str
    price: Decimal
    quantity: int
    description: Union[str, None]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Hotdog",
                    "category": "Lanche",
                    "description": "Lorem ipsum...",
                    "price": "24.99",
                    "quantity": 10,
                },
            ]
        }
    }


class ProductResponseDTO(BaseModel):
    id: Union[int, None] = None
    name: str
    category: str
    description: Union[str, None]
    price: Decimal
    quantity: int
