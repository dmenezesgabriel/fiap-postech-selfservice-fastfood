import os
from typing import List
from src.common.interfaces.user_gateway import UserGatewayInterface
from src.common.interfaces.user_repository import UserRepositoryInterface
from src.config import AWSConfig
from src.core.domain.entities.user import UserEntity


class UserGateway(UserGatewayInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> UserEntity:
        return self.user_repository.get_by_id(id=id)

    def get_by_email(self, email: str) -> UserEntity:
        return self.user_repository.get_by_email(email=email)

    def get_by_cpf(self, cpf: str) -> UserEntity:
        return self.user_repository.get_by_cpf(cpf=cpf)

    def list_all(self) -> List[UserEntity]:
        return self.user_repository.list_all()

    def create(self, user: UserEntity) -> UserEntity:

        client = AWSConfig.create_resource('cognito-idp')

        cognito_attributes = [
            {'Name': 'preferred_username', 'Value': user.cpf},
            {'Name': 'email', 'Value': user.email}
        ]
        user_pool_id = os.getenv('COGNITO_USER_POOL')
        client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=user.cpf,
            TemporaryPassword=user.password,
            UserAttributes=cognito_attributes,
            MessageAction='SUPPRESS'
        )

        return self.user_repository.create(user=user)

    def delete(self, id: int) -> bool:
        return self.user_repository.delete(id=id)
