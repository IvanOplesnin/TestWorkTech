import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from backend.schemas import ResponseUser


class TimeProjectBase(BaseModel):

    user_id: int = Field(..., description="Идентификатор пользователя")
    project_id: int = Field(..., description="Идентификатор проекта")
    date: Optional[datetime.date] = Field(None, description="Дата. Формат: YYYY-MM-DD")
    hours: int = Field(..., description="Количество часов а проекте за день")


class CreateTimeProject(TimeProjectBase):
    pass


class ResponseTimeProjectForProject(TimeProjectBase):
    id: int = Field(..., description="Идентификатор записи")

    user: ResponseUser = Field(..., description="Пользователь")
    model_config = ConfigDict(from_attributes=True)
