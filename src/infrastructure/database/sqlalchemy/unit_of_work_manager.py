from sqlalchemy.orm import sessionmaker

from src.application.ports.unit_of_work_manager import UnitOfWorkManager
from src.infrastructure.database.sqlalchemy.orm import engine
from src.infrastructure.database.sqlalchemy.unit_of_work import (
    SQLAlchemyUnitOfWork,
)


class SQLAlchemyUnitOfWorkManager(UnitOfWorkManager):
    _engine = engine

    def __init__(self) -> None:
        """
        @see: https://docs.sqlalchemy.org/en/20/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it
        """
        self._session_factory = sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    def start(self):
        SessionLocal = self._session_factory()
        return SQLAlchemyUnitOfWork(session=SessionLocal)
