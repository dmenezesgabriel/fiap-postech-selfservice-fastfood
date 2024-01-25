from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from src.infrastructure.database.sqlalchemy.orm import Base

from .base import BaseModel


class OrderDetail(Base, BaseModel):
    __tablename__ = "order_details"

    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float)
    # payment_id = Column(Integer,ForeignKey("payment_details.id"))


class OrderItem(Base, BaseModel):
    __tablename__ = "order_items"

    order_id = Column(Integer, ForeignKey("order_details.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
