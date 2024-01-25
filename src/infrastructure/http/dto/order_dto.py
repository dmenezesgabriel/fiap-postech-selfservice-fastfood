from typing import Union, List
from pydantic import BaseModel, EmailStr, ConfigDict, validator


class ProductDTO(BaseModel):
    id: int
    price: float
    quantity: int


class OrderDTO(BaseModel):
    user_id: int
    products: List[ProductDTO]


class OrderResponseDTO(BaseModel):
    user_id: int
    transacion_amount: float
    payment_method: str
    description : str
    products : List[ProductDTO]