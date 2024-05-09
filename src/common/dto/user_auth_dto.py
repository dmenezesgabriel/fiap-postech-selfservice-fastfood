from pydantic import BaseModel


class UserAuthDTO(BaseModel):
    email: str
    password: str
