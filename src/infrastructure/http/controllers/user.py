from typing import List

from src.application.ports.user_service import UserServiceInterface
from src.domain.entities.user import User
from src.infrastructure.http.dto.user_dto import UserDTO, UserDTOResponse


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

    def get_by_cpf(self, cpf: str) -> User:
        user = self.user_service.get_by_cpf(cpf)
        return user

    def get_by_email(self, email: str) -> User:
        user = self.user_service.get_by_email(email)
        return user

    def get_all(self) -> List[UserDTOResponse]:
        users = self.user_service.get_all()
        users_list: list = list()
        for user in users:
            users_list.append(
                UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)
            )

        return users_list

    def create(self, user: UserDTO) -> User:
        user = self.user_service.create(user)
        return user

    def update(self, user: User) -> User:
        user = self.user_service.update(user)
        return user

    def delete(self, id: int) -> bool:
        return self.user_service.delete(id)
