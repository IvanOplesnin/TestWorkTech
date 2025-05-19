from pydantic import BaseModel, Field, ConfigDict

from backend.schemas.time_project import ResponseTimeProjectForProject


class ProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)


class ResponseProject(ProjectBase):

    time_users: list[ResponseTimeProjectForProject] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
