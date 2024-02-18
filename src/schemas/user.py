from pydantic import BaseModel, field_validator, ValidationError, Field
from typing import List


class Info(BaseModel):
    id: int
    email: str = Field(min_length=5)
    first_name: str
    last_name: str
    avatar: str = ""

    @field_validator("id")
    def check_id_is_not_negative(cls, user_id):
        if user_id < 0:
            raise ValidationError("Некорректный ID")
        else:
            return user_id

    @field_validator("email")
    def check_dog_in_email(cls, user_email):
        if '@' in user_email:
            return user_email
        else:
            raise ValueError("Некорректный email")




class Support(BaseModel):
    url: str
    text: str

class UserModel(BaseModel):
    data: Info
    support: Support

class Resp(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Info]
    support: Support


class User(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

class UpdateUser(BaseModel):
    name: str
    job: str
    updatedAt: str

class Register(BaseModel):
    id: int
    token: str

class Login(BaseModel):
    token: str
