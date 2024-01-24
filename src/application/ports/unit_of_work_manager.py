import abc

from src.application.ports.unit_of_work import UnitOfWork


class UnitOfWorkManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self) -> UnitOfWork:
        raise NotImplementedError
