from typing import Union

from pydantic import BaseModel, EmailStr, validator

from src.domain.value_objects.cpf import Cpf
from src.domain.value_objects.email import Email
from src.domain.value_objects.full_name import FullName


class CreateUserDTO(BaseModel):
    id: Union[int, None] = None
    email: EmailStr
    full_name: FullName
    password: str
    cpf: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "example@example.com",
                    "password": "123",
                    "full_name": {
                        "first_name": "John",
                        "last_name": "Doe",
                    },
                    "cpf": "00000000000",
                }
            ]
        }
    }

    @validator("email")
    def validate_email(cls, email):
        Email.validate(email)
        return email

    @validator("cpf")
    def validate_cpf(cls, cpf):
        Cpf.validate(cpf)
        return cpf


class UserResponseDTO(BaseModel):
    id: int
    cpf: str
    email: str
