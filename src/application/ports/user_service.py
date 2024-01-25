import abc
from typing import List

from src.domain.entities.user import User
from src.infrastructure.http.dto.user_dto import UserDTO, UserDTOResponse


class UserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, user_repository: str):
        raise NotImplementedError

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
    def get_all(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: UserDTO) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError
