from typing import List

from fastapi import APIRouter, HTTPException

from src.common.dto.user_dto import CreateUserDTO, UserResponseDTO
from src.core.domain.entities.user import UserEntity
from src.core.use_cases.user import UserService
from src.external.database.sqlalchemy.repositories.user import UserRepository

user_repository = UserRepository()
user_service = UserService(user_repository)


router = APIRouter(prefix="/users", tags=["users"])


# TODO : Implementar paginação
@router.get("/", response_model=List[UserResponseDTO])
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
            UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)
        )

    return users_list


@router.get("/{user_id}", response_model=UserResponseDTO)
async def read_user(user_id: int):
    """
    # Busca do usuário pelo id

    ## Observações:

    *
    """
    user = user_service.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)


@router.post("/")
async def create_user(user: CreateUserDTO) -> UserResponseDTO:
    """
    # Criação de usuário

    ## Observações:

    * Os e-mails e CPFs dos usuários são únicos na base de dados
    """

    user: UserEntity = user_service.create(user)
    return UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)


@router.get("/cpf/{cpf}", response_model=UserResponseDTO)
async def get_user_by_cpf(cpf: str):
    """
    # Busca do usuário pelo CPF.

    ## Observações:

    * O número do CPF não deverá possuir caracteres especiais, como "." e "-".
    """

    user = user_service.get_by_cpf(cpf)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)


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
