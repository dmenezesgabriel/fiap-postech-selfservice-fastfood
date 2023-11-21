from sqlalchemy import Column, Integer, String
from src.adapter.driven.infra.database.sqlalchemy.orm import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(32), nullable=False)
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)

    @property
    def full_name(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name
        }
