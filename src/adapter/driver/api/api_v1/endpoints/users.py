from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.params import Query

from src.adapter.driven.infra.database.sqlalchemy.models.user import (
    User as UserModel,
)
from src.adapter.driven.infra.database.sqlalchemy.repositories.user import (
    UserRepository,
)
from src.adapter.driven.infra.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager,
)
from src.adapter.driver.api.controllers.user import UserController
from src.core.application.services.user import UserService
from src.core.domain.entities.user import User
from src.adapter.driver.api.dto.user_dto import UserDTO, UserDTOResponse
from src.core.domain.value_objects.cpf import Cpf

work_manager = SQLAlchemyUnitOfWorkManager()
user_repository = UserRepository(work_manager)
user_service = UserService(user_repository)
user_controller = UserController(user_service)

router = APIRouter(prefix="/users", tags=["users"])


# TODO : Implementar paginação
@router.get("/", response_model=List[UserDTOResponse])
async def read_users():
    return user_controller.get_all()


@router.get("/{user_id}", response_model=UserDTOResponse)
async def read_user(user_id: int):
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTOResponse(
        id=user.id,
        email=user.email,
        cpf=user.cpf
    )


@router.post("/")
async def create_user(user: UserDTO) -> UserDTOResponse:
    """
    # Criação de usuário

    ## Observações:

    * Os e-mails e CPFs dos usuários são únicos na base de dados
    """

    user: User = user_controller.create(user)
    return UserDTOResponse(
        id=user.id,
        email=user.email,
        cpf=user.cpf
    )


@router.get("/cpf/{cpf}", response_model=UserDTOResponse)
async def get_user_by_cpf(
        cpf: str
):
    """
    # Identificação do usuário pelo CPF.

    ## Observações:

    * O número do CPF não deverá possuir caracteres especiais, como "." e "-".
    """

    user = user_controller.get_by_cpf(cpf)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTOResponse(
        id=user.id,
        email=user.email,
        cpf=user.cpf
    )


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete(user_id)
