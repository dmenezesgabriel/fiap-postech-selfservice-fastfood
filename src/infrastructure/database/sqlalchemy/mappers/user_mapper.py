from src.domain.entities.user import User as UserEntity
from src.domain.value_objects.full_name import FullName
from src.infrastructure.database.sqlalchemy.models.user import User as UserModel


class UserMapper:
    @staticmethod
    def model_to_entity(user_model):
        return UserEntity(
            id=user_model.id,
            email=user_model.email,
            password=user_model.password,
            full_name=FullName(
                first_name=user_model.first_name,
                last_name=user_model.last_name,
            ),
            cpf=user_model.cpf,
        )

    @staticmethod
    def entity_to_model(user_entity):
        return UserModel(
            id=user_entity.id,
            email=user_entity.email,
            password=user_entity.password,
            first_name=user_entity.full_name.first_name,
            last_name=user_entity.full_name.last_name,
            cpf=user_entity.cpf,
        )
