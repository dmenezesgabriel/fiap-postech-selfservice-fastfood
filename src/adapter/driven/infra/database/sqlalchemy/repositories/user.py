from typing import List

from src.adapter.driven.infra.database.sqlalchemy.models.user import User
from src.core.application.ports.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""

    def __init__(self, work_manager):
        self._work_manager = work_manager

    def get_by_id(self, id: int) -> User:
        with self._work_manager.start() as session:
            return session.query(User).filter_by(id=id).first()

    def get_by_email(self, email: str) -> User:
        with self._work_manager.start() as session:
            return session.query(User).filter_by(email=email).first()

    def get_all(self) -> List[User]:
        with self._work_manager.start() as session:
            return session.query(User).all()

    def create(self, user: User) -> User:
        with self._work_manager.start() as session:
            session.add(user)
        return user

    def update(self, user: User) -> User:
        with self._work_manager.start() as session:
            session.add(user)
            return user

    def delete(self, id: int) -> bool:
        with self._work_manager.start() as session:
            user = session.query(User).filter_by(id=id).first()
            if user is None:
                return False
            session.delete(user)
            return True
