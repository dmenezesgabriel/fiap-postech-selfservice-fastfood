from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from src.adapter.driven.infra.database.sqlalchemy.orm import Base
from .base import BaseModel

class OrderDetails(Base,BaseModel):
    __tablename__ = "order_details"

    user_id = Column(Integer,ForeignKey("users.id"))
    total = Column(Float)
    # payment_id = Column(Integer,ForeignKey("payment_details.id"))

class OrderItems(Base,BaseModel):
    __tablename__ = "order_items"

    order_id = Column(Integer,ForeignKey("order_details.id"))
    product_id = Column(Integer,ForeignKey("product.id"))
