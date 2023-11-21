from typing import Union

from pydantic import BaseModel, EmailStr, ConfigDict, validator
from src.core.domain.value_objects.email import Email
from src.core.domain.value_objects.full_name import FullName


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    email: EmailStr
    password: str
    full_name: FullName

    @validator("email")
    def validate_email(cls, email):
        Email.validate(email)
        return email
