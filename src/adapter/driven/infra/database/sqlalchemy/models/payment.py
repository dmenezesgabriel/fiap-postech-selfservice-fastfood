from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,Enum
from src.adapter.driven.infra.database.sqlalchemy.orm import Base
import enum
from .base import BaseModel

class PaymentStatusEnum(enum.Enum):
    captured = "CAPTURED"
    declined = "DECLINED"
    pending = "PENDING"

class PaymentDetails(Base,BaseModel):
    __tablename__ = "payment_details"

    order_id = Column(Integer,ForeignKey("order_details.id"))
    amount = Column(Float)
    provider = Column(String(50))
    status = Column(Enum(PaymentStatusEnum))
