import abc
from typing import List

from src.domain.entities.user import User


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_email(self, email: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_cpf(self, cpf: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError
