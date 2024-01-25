from typing import Union

from pydantic import BaseModel, EmailStr, validator

from src.domain.value_objects.cpf import Cpf
from src.domain.value_objects.email import Email
from src.domain.value_objects.full_name import FullName


class UserDTO(BaseModel):
    id: Union[int, None] = None
    email: EmailStr
    full_name: FullName
    password: str
    cpf: str

    @validator("email")
    def validate_email(cls, email):
        Email.validate(email)
        return email

    @validator("cpf")
    def validate_cpf(cls, cpf):
        Cpf.validate(cpf)
        return cpf


class UserDTOResponse(BaseModel):
    id: int
    cpf: str
    email: str
