from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.external.database.sqlalchemy.models.base import BaseModel
from src.external.database.sqlalchemy.orm import Base


class ProductModel(Base, BaseModel):
    __tablename__ = "product"

    name = Column(String(100), unique=True, index=True)
    description = Column(String(255), nullable=True)
    sku = Column(String(30), unique=True, nullable=True)
    category_id = Column(Integer, ForeignKey("product_category.id"))
    price = Column(Float)
    discount_id = Column(Integer, ForeignKey("discount.id"))
    quantity = Column(Integer)
    category = relationship("ProductCategoryModel", lazy="joined")


class ProductCategoryModel(Base, BaseModel):
    __tablename__ = "product_category"

    name = Column(String(30), unique=True, index=True)


class DiscountModel(Base, BaseModel):
    __tablename__ = "discount"

    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), nullable=True)
    discount_percent = Column(Float)
