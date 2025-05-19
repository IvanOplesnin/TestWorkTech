from pydantic import BaseModel, Field


class ResponseReportRow(BaseModel):
    id: int = Field(..., description="User id")
    hours: int = Field(..., description="Кол-во часов")





