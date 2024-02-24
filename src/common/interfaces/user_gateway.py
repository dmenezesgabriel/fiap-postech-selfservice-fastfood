import abc
from typing import List

from src.core.domain.entities.user import UserEntity


class UserGatewayInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> UserEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_cpf(self, cpf: str) -> UserEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[UserEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError
