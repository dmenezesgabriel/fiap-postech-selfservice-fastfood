from typing import Union

from pydantic import BaseModel, EmailStr, ConfigDict, validator

from src.core.domain.base.exceptions import InvalidCpfError
from src.core.domain.value_objects.email import Email
from src.core.domain.value_objects.cpf import Cpf
from src.core.domain.value_objects.full_name import FullName
from src.adapter.driver.api.dto.base import Omit


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
    id : int
    cpf : str
    email : str


class GetUserByCpfDTO(BaseModel):
    cpf: str
    
    @validator("cpf")
    def validate_cpf(cls, cpf):
        Cpf.validate(cpf)
        return cpf