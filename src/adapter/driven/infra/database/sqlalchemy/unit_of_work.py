from src.core.application.ports.unit_of_work import UnitOfWork
from src.core.domain.base.exceptions import OperationalException
from sqlalchemy.exc import SQLAlchemyError


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        try:
            self.session.commit()
        except SQLAlchemyError as error:
            self.session.rollback()
            raise OperationalException(error)

    def commit(self):
        self.session.commit()
        self.session.close()

    def rollback(self):
        self.session.rollback()
        self.session.close()
