from sqlalchemy import Column, Integer, String
from src.adapter.driven.infra.database.sqlalchemy.orm import Base
from .base import BaseModel


class User(Base,BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(32), nullable=False)
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)
    cpf = Column(String(14), nullable=False)

    @property
    def full_name(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name
        }

