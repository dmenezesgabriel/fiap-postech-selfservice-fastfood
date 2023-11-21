from typing import List

from fastapi import APIRouter, HTTPException
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

work_manager = SQLAlchemyUnitOfWorkManager()
user_repository = UserRepository(work_manager)
user_service = UserService(user_repository)
user_controller = UserController(user_service)


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[User])
async def read_users():
    return user_controller.get_all()


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/")
async def create_user(user: User):
    if user_controller.get_by_email(user.email) is not None:
        raise HTTPException(
            status_code=400, detail="User with this email already exists"
        )
    return user_controller.create(
        UserModel(
            email=user.email,
            password=user.password,
            first_name=user.full_name.first_name,
            last_name=user.full_name.last_name
        )
    )


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    user = user_controller.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete(user_id)
