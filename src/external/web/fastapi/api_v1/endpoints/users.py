from typing import List

from fastapi import APIRouter, HTTPException

from src.common.dto.user_dto import CreateUserDTO, UserResponseDTO
from src.communication.controller.user import UserController
from src.external.database.sqlalchemy.repositories.user import UserRepository

user_repository = UserRepository()
user_controller = UserController(user_repository)


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserResponseDTO])
async def list_users():
    users = user_controller.list_users()
    return [
        UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)
        for user in users
    ]


@router.get("/{user_id}", response_model=UserResponseDTO)
async def get_user_by_id(user_id: int):
    user = user_controller.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)


@router.post("/")
async def create_user(user: CreateUserDTO) -> UserResponseDTO:
    new_user = user_controller.create_user(user)
    return UserResponseDTO(id=new_user.id, email=user.email, cpf=user.cpf)


@router.get("/cpf/{cpf}", response_model=UserResponseDTO)
async def get_user_by_cpf(cpf: str):
    user = user_controller.get_user_by_cpf(cpf)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponseDTO(id=user.id, email=user.email, cpf=user.cpf)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    user = user_controller.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete_user(user_id)
