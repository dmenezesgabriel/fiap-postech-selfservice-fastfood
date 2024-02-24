from typing import List

from src.common.interfaces.user_gateway import UserGatewayInterface
from src.core.domain.entities.user import UserEntity
from src.core.domain.exceptions import UserAlreadyExistsError


class UserUseCase:
    @staticmethod
    def get_by_id(id: int, user_gateway: UserGatewayInterface) -> UserEntity:
        return user_gateway.get_by_id(id)

    @staticmethod
    def get_by_email(
        email: str, user_gateway: UserGatewayInterface
    ) -> UserEntity:
        return user_gateway.get_by_email(email)

    @staticmethod
    def get_by_cpf(cpf: str, user_gateway: UserGatewayInterface) -> UserEntity:
        return user_gateway.get_by_cpf(cpf)

    @staticmethod
    def list_all(user_gateway: UserGatewayInterface) -> List[UserEntity]:
        return user_gateway.list_all()

    @staticmethod
    def create(
        user: UserEntity, user_gateway: UserGatewayInterface
    ) -> UserEntity:
        if user_gateway.get_by_email(user.email) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this e-mail ({user.email})."
            )

        if user_gateway.get_by_cpf(user.cpf) is not None:
            raise UserAlreadyExistsError(
                f"User already exists with this cpf ({user.cpf})."
            )

        return user_gateway.create(user)

    @staticmethod
    def update(
        user: UserEntity, user_gateway: UserGatewayInterface
    ) -> UserEntity:
        return user_gateway.update(user)

    @staticmethod
    def delete(id: int, user_gateway: UserGatewayInterface) -> bool:
        return user_gateway.delete(id)
