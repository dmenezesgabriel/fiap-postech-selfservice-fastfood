from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)

from src.infrastructure.database.sqlalchemy.models.base import BaseModel
from src.infrastructure.database.sqlalchemy.orm import Base


class ShoppingSession(Base, BaseModel):
    __tablename__ = "shopping_session"

    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)


class CartItem(Base, BaseModel):
    __tablename__ = "cart_item"

    session_id = Column(Integer, ForeignKey("shopping_session.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
