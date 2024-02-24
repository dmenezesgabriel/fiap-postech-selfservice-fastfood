from src.common.dto.user_dto import CreateUserDTO
from src.common.interfaces.user_repository import UserRepositoryInterface
from src.communication.gateway.user import UserGateway
from src.core.use_cases.user import UserUseCase


class UserController:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def list_users(self):
        user_gateway = UserGateway(self.user_repository)
        return UserUseCase.list_all(user_gateway=user_gateway)

    def get_user_by_id(self, user_id: int):
        user_gateway = UserGateway(self.user_repository)
        return UserUseCase.get_by_id(id=user_id, user_gateway=user_gateway)

    def create_user(self, user: CreateUserDTO):
        user_gateway = UserGateway(self.user_repository)
        return UserUseCase.create(user=user, user_gateway=user_gateway)

    def get_user_by_cpf(self, cpf: str):
        user_gateway = UserGateway(self.user_repository)
        return UserUseCase.get_by_cpf(cpf=cpf, user_gateway=user_gateway)

    def delete_user(self, user_id: int):
        user_gateway = UserGateway(self.user_repository)
        return UserUseCase.delete(id=user_id, user_gateway=user_gateway)
