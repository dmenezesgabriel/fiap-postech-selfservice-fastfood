from fastapi import APIRouter, HTTPException

from src.common.dto.user_auth_dto import UserAuthDTO
from src.communication.controller.user import UserController
from src.external.database.sqlalchemy.repositories.user import UserRepository

user_repository = UserRepository()
user_controller = UserController(user_repository)

router = APIRouter(prefix="/authenticate", tags=["auth"])


@router.post("/")
async def auth_user(user_auth: UserAuthDTO) -> dict[str, str]:
    user = user_controller.get_user_by_id(user_id=user_auth.email)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"Message": f"{user_auth.email}"}
