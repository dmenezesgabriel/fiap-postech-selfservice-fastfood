from typing import List

from src.common.interfaces.user_repository import UserRepositoryInterface
from src.core.domain.entities.user import UserEntity
from src.core.domain.exceptions import UserAlreadyExistsError


class UserService:
    """User use case or service implementation."""

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> UserEntity:
        return self.user_repository.get_by_id(id)

    def get_by_email(self, email: str) -> UserEntity:
        return self.user_repository.get_by_email(email)

    def get_by_cpf(self, cpf: str) -> UserEntity:
        return self.user_repository.get_by_cpf(cpf)

    def list_all(self) -> List[UserEntity]:
        return self.user_repository.list_all()

    def create(self, user: UserEntity) -> UserEntity:
        if self.user_repository.get_by_email(user.email) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this e-mail ({user.email})."
            )

        if self.user_repository.get_by_cpf(user.cpf) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this cpf ({user.cpf})."
            )

        return self.user_repository.create(user)

    def update(self, user: UserEntity) -> UserEntity:
        return self.user_repository.update(user)

    def delete(self, id: int) -> bool:
        return self.user_repository.delete(id)
