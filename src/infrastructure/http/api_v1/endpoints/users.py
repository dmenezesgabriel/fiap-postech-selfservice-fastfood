from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.params import Query

from src.application.services.user import UserService
from src.domain.entities.user import User
from src.infrastructure.database.sqlalchemy.models.user import User as UserModel
from src.infrastructure.database.sqlalchemy.repositories.user import (
    UserRepository,
)
from src.infrastructure.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager,
)
from src.infrastructure.http.controllers.user import UserController
from src.infrastructure.http.dto.user_dto import UserDTO, UserDTOResponse

work_manager = SQLAlchemyUnitOfWorkManager()
user_repository = UserRepository(work_manager)
user_service = UserService(user_repository)
user_controller = UserController(user_service)

router = APIRouter(prefix="/users", tags=["users"])


# TODO : Implementar paginação
@router.get("/", response_model=List[UserDTOResponse])
async def read_users():
    """
    # Listagem de usuários

    ## Observações:

    *
    """
    return user_controller.get_all()


@router.get("/{user_id}", response_model=UserDTOResponse)
async def read_user(user_id: int):
    """
    # Busca do usuário pelo id

    ## Observações:

    *
    """
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)


@router.post("/")
async def create_user(user: UserDTO) -> UserDTOResponse:
    """
    # Criação de usuário

    ## Observações:

    * Os e-mails e CPFs dos usuários são únicos na base de dados
    """

    user: User = user_controller.create(user)
    return UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)


@router.get("/cpf/{cpf}", response_model=UserDTOResponse)
async def get_user_by_cpf(cpf: str):
    """
    # Busca do usuário pelo CPF.

    ## Observações:

    * O número do CPF não deverá possuir caracteres especiais, como "." e "-".
    """

    user = user_controller.get_by_cpf(cpf)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """
    # Exclusão do usuário pelo id

    ## Observações:

    *
    """
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete(user_id)
