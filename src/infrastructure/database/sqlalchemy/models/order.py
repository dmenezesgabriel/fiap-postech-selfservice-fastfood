from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.infrastructure.database.sqlalchemy.models.base import BaseModel
from src.infrastructure.database.sqlalchemy.orm import Base


class OrderDetail(Base, BaseModel):
    __tablename__ = "order_details"

    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float)
    order_items = relationship("OrderItem", lazy="joined")


class OrderItem(Base, BaseModel):
    __tablename__ = "order_items"

    order_id = Column(Integer, ForeignKey("order_details.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    order_detail = relationship("OrderDetail", back_populates="order_items")
    product = relationship("Product", lazy="joined")
