from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from src.infrastructure.config.settings import Config

Base = declarative_base()

engine = create_engine(Config.DATABASE_URL, echo=True)
