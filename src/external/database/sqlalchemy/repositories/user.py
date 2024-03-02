from typing import List

from src.common.interfaces.user_repository import UserRepositoryInterface
from src.core.domain.entities.user import UserEntity
from src.external.database.sqlalchemy.mappers.user_mapper import UserMapper
from src.external.database.sqlalchemy.models.user import UserModel
from src.external.database.sqlalchemy.session_mixin import use_database_session


class UserRepository(UserRepositoryInterface):
    def get_by_id(self, id: int) -> UserEntity:
        with use_database_session() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            return UserMapper.model_to_entity(user) if user else None

    def get_by_email(self, email: str) -> UserEntity:
        with use_database_session() as session:
            user = session.query(UserModel).filter_by(email=email).first()
            return UserMapper.model_to_entity(user) if user else None

    def get_by_cpf(self, cpf: str) -> UserEntity:
        with use_database_session() as session:
            user = session.query(UserModel).filter_by(cpf=cpf).first()
            return UserMapper.model_to_entity(user) if user else None

    def list_all(self) -> List[UserEntity]:
        with use_database_session() as session:
            users = session.query(UserModel).all()
            return [UserMapper.model_to_entity(user) for user in users]

    def create(self, user: UserEntity) -> UserEntity:
        with use_database_session() as session:
            user_model = UserMapper.entity_to_model(user)
            session.add(user_model)
            session.commit()
            session.flush()  # Get back the model id
            return UserMapper.model_to_entity(user_model)

    def delete(self, id: int) -> bool:
        with use_database_session() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            if user is None:
                return False
            session.delete(user)
            session.commit()
            return True
