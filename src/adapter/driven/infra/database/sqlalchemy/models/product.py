from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.adapter.driven.infra.database.sqlalchemy.orm import Base
from .base import BaseModel


class Product(Base, BaseModel):
    __tablename__ = "product"

    name = Column(String(100), unique=True, index=True)
    description = Column(String(255), nullable=True)
    sku = Column(String(30), unique=True, nullable=True)
    category_id = Column(Integer, ForeignKey("product_category.id"))
    price = Column(Float)
    discount_id = Column(Integer, ForeignKey("discount.id"))
    quantity = Column(Integer)
    category = relationship("ProductCategory", lazy="joined")


class ProductCategory(Base, BaseModel):
    __tablename__ = "product_category"

    name = Column(String(30), unique=True, index=True)


class Discount(Base,BaseModel):
    __tablename__ = "discount"

    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), nullable=True)
    discount_percent = Column(Float)
