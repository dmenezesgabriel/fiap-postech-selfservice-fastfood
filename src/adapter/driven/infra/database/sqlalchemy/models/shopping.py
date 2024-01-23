from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,Enum
from src.adapter.driven.infra.database.sqlalchemy.orm import Base
from .base import BaseModel


class ShoppingSession(Base,BaseModel):
    __tablename__ = "shopping_session"

    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)

class CartItem(Base,BaseModel):
    __tablename__ = "cart_item"

    session_id = Column(Integer, ForeignKey("shopping_session.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer,nullable=False)

