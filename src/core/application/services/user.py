from typing import List

from src.core.application.ports.user_repository import UserRepositoryInterface
from src.core.application.ports.user_service import UserServiceInterface
from src.core.domain.entities.user import User


class UserService(UserServiceInterface):
    """User use case or service implementation."""

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> User:
        return self.user_repository.get_by_id(id)

    def get_by_email(self, email: str) -> User:
        return self.user_repository.get_by_email(email)

    def get_all(self) -> List[User]:
        return self.user_repository.get_all()

    def create(self, user: User) -> User:
        return self.user_repository.create(user)

    def update(self, user: User) -> User:
        return self.user_repository.update(user)

    def delete(self, id: int) -> bool:
        return self.user_repository.delete(id)
