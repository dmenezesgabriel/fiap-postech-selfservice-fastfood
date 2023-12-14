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


# TODO : Alterar para response DTO
@router.get("/", response_model=List[User])
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
# async def create_user(user: User):
async def create_user(user: UserDTO) -> UserDTOResponse:
    if user_controller.get_by_email(user.email) is not None:
        raise HTTPException(
            status_code=400, detail="User with this email already exists"
        )
    user: User = user_controller.create(
        UserModel(
            email=user.email,
            password=user.password,
            first_name=user.full_name.first_name,
            last_name=user.full_name.last_name,
            cpf=user.cpf
        )
    )
    return UserDTOResponse(
        id=user.id,
        email=user.email,
        cpf=user.cpf
    )


@router.get("/cpf/{cpf}", response_model=UserDTOResponse)
async def get_user_by_cpf(
        cpf : str
):
    """
    # Endpoint que identifica o usuário pelo CPF.

    ## Observações:

    * O número do CPF não deverá possuir caracteres especiais, como "." e "-".
    """

    # TODO : validação deve ficar aqui?
    try:
        Cpf.validate(cpf)
    except ValueError as e:
        raise RequestValidationError(errors=str(e))

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
