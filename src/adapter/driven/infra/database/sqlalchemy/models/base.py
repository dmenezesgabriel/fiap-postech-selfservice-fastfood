from src.adapter.driven.infra.database.sqlalchemy.orm import Base
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime, timezone


class BaseModel:
    __abstract__ = True
    id = Column(Integer,primary_key=True,autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)

    def before_save(self,*args,**kwargs):
        print("Calling before save....")
        pass