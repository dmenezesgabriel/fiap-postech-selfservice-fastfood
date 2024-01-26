from typing import List

from src.application.ports.user_repository import UserRepositoryInterface
from src.application.ports.user_service import UserServiceInterface
from src.domain.base.exceptions import UserAlreadyExistsError
from src.domain.entities.user import User
from src.infrastructure.database.sqlalchemy.models.user import User as UserModel
from src.infrastructure.http.dto.user_dto import UserDTO


class UserService(UserServiceInterface):
    """User use case or service implementation."""

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> User:
        return self.user_repository.get_by_id(id)

    def get_by_email(self, email: str) -> User:
        return self.user_repository.get_by_email(email)

    def get_by_cpf(self, cpf: str) -> User:
        return self.user_repository.get_by_cpf(cpf)

    def list_all(self) -> List[User]:
        return self.user_repository.list_all()

    def create(self, user: UserDTO) -> User:
        if self.user_repository.get_by_email(user.email) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this e-mail ({user.email})."
            )

        if self.user_repository.get_by_cpf(user.cpf) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this cpf ({user.cpf})."
            )

        return self.user_repository.create(
            UserModel(
                email=user.email,
                password=user.password,
                first_name=user.full_name.first_name,
                last_name=user.full_name.last_name,
                cpf=user.cpf,
            )
        )

    def update(self, user: User) -> User:
        return self.user_repository.update(user)

    def delete(self, id: int) -> bool:
        return self.user_repository.delete(id)
