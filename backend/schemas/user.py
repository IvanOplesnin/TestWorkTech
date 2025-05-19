from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    first_name: str = Field(..., description="First name")
    last_name: Optional[str] = Field(None, description="Last name")
    username: str = Field(..., description="Username")
    manager: bool = Field(False, description="Is manager")


class CreateUser(UserBase):
    password: str = Field(..., description="Password")


class UpdateUser(UserBase):
    first_name: Optional[str] = Field(None, description="First name")
    last_name: Optional[str] = Field(None, description="Last name")
    username: Optional[str] = Field(None, description="Username")
    manager: Optional[bool] = Field(None, description="Is manager")
    password: Optional[str] = Field(None, description="Password")


class ResponseUser(UserBase):
    id: int = Field(..., description="User ID")

    model_config = ConfigDict(from_attributes=True)
