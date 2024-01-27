from typing import List

from src.application.ports.user_repository import UserRepositoryInterface
from src.domain.entities.user import User as UserEntity
from src.infrastructure.database.sqlalchemy.mappers.user_mapper import (
    UserMapper,
)
from src.infrastructure.database.sqlalchemy.models.user import User as UserModel
from src.infrastructure.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager,
)


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""

    def __init__(self):
        self._work_manager = SQLAlchemyUnitOfWorkManager()

    def get_by_id(self, id: int) -> UserModel:
        with self._work_manager.start() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            return UserMapper.model_to_entity(user)

    def get_by_email(self, email: str) -> UserEntity:
        with self._work_manager.start() as session:
            user = session.query(UserModel).filter_by(email=email).first()
            return UserMapper.model_to_entity(user) if user else None

    def get_by_cpf(self, cpf: str) -> UserEntity:
        with self._work_manager.start() as session:
            user = session.query(UserModel).filter_by(cpf=cpf).first()
            return UserMapper.model_to_entity(user) if user else None

    def list_all(self) -> List[UserEntity]:
        with self._work_manager.start() as session:
            users = session.query(UserModel).all()
            return [UserMapper.model_to_entity(user) for user in users]

    def create(self, user: UserEntity) -> UserEntity:
        with self._work_manager.start() as session:
            user_model = UserMapper.entity_to_model(user)
            session.add(user_model)
            session.flush()  # Get back the model id
            return UserMapper.model_to_entity(user_model)

    def delete(self, id: int) -> bool:
        with self._work_manager.start() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            if user is None:
                return False
            session.delete(user)
            return True
