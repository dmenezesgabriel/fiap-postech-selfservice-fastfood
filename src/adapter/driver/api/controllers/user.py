from typing import List

from src.core.application.ports.user_service import UserServiceInterface
from src.core.domain.entities.user import User


class UserController:
    def __init__(
        self,
        # logger: LoggerInterface,
        user_service: UserServiceInterface,
    ):
        # self.logger = logger
        self.user_service = user_service

    def get_by_id(self, id: int) -> User:
        user = self.user_service.get_by_id(id)
        return user

    def get_by_email(self, email: str) -> User:
        user = self.user_service.get_by_email(email)
        return user

    def get_all(self) -> List[User]:
        users = self.user_service.get_all()
        return users

    def create(self, user: User) -> User:
        user = self.user_service.create(user)
        return user

    def update(self, user: User) -> User:
        user = self.user_service.update(user)
        return user

    def delete(self, id: int) -> bool:
        return self.user_service.delete(id)
