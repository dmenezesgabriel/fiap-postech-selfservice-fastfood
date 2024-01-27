from decimal import Decimal
from typing import Union

from pydantic import BaseModel


class ProductDTO(BaseModel):
    id: Union[int, None] = None
    name: str
    category: str
    price: Decimal
    quantity: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Hotdog",
                    "category": "Lanche",
                    "price": "24.99",
                    "quantity": 10,
                },
            ]
        }
    }


class ProductDTOResponse(BaseModel):
    id: Union[int, None] = None
    name: str
    category: str
    price: Decimal
    quantity: int
