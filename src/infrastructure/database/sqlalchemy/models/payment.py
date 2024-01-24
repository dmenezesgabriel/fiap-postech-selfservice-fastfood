import enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)

from src.infrastructure.database.sqlalchemy.orm import Base

from .base import BaseModel


class PaymentStatusEnum(enum.Enum):
    captured = "CAPTURED"
    declined = "DECLINED"
    pending = "PENDING"


class PaymentDetails(Base, BaseModel):
    __tablename__ = "payment_details"

    order_id = Column(Integer, ForeignKey("order_details.id"))
    amount = Column(Float)
    provider = Column(String(50))
    status = Column(Enum(PaymentStatusEnum))
