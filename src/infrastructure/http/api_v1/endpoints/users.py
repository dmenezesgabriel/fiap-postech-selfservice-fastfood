from typing import List

from fastapi import APIRouter, HTTPException

from src.application.services.user import UserService
from src.domain.entities.user import User
from src.infrastructure.database.sqlalchemy.repositories.user import (
    UserRepository,
)
from src.infrastructure.http.dto.user_dto import UserDTO, UserDTOResponse

user_repository = UserRepository()
user_service = UserService(user_repository)


router = APIRouter(prefix="/users", tags=["users"])


# TODO : Implementar paginação
@router.get("/", response_model=List[UserDTOResponse])
async def read_users():
    """
    # Listagem de usuários

    ## Observações:

    *
    """
    users = user_service.list_all()
    users_list: list = list()
    for user in users:
        users_list.append(
            UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)
        )

    return users_list


@router.get("/{user_id}", response_model=UserDTOResponse)
async def read_user(user_id: int):
    """
    # Busca do usuário pelo id

    ## Observações:

    *
    """
    user = user_service.get_by_id(user_id)
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

    user: User = user_service.create(user)
    return UserDTOResponse(id=user.id, email=user.email, cpf=user.cpf)


@router.get("/cpf/{cpf}", response_model=UserDTOResponse)
async def get_user_by_cpf(cpf: str):
    """
    # Busca do usuário pelo CPF.

    ## Observações:

    * O número do CPF não deverá possuir caracteres especiais, como "." e "-".
    """

    user = user_service.get_by_cpf(cpf)
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
    user = user_service.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.delete(user_id)
