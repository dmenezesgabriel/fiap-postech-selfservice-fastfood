import abc
from typing import List

from src.core.domain.entities.user import User


class UserServiceInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return (
            hasattr(__subclass, "get_by_id")
            and callable(__subclass.get_by_id)
            and hasattr(__subclass, "get_by_email")
            and callable(__subclass.get_by_email)
            and hasattr(__subclass, "get_all")
            and callable(__subclass.get_all)
            and hasattr(__subclass, "create")
            and callable(__subclass.create)
            and hasattr(__subclass, "update")
            and callable(__subclass.update)
            and hasattr(__subclass, "delete")
            and callable(__subclass.delete)
            or NotImplemented
        )

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
    def get_all(self) -> List[User]:
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
