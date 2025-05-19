import datetime

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import User, Project, TimeProject
from backend.schemas.report import ResponseReportRow


async def get_report(
        start_date: datetime.date,
        end_date: datetime.date,
        project_id: int,
        session: AsyncSession
) -> list[ResponseReportRow]:
    stmt = (
        select(
            TimeProject.user_id.label("id"),
            func.sum(TimeProject.hours).label("hours")
        )
        .where(
            TimeProject.project_id == project_id,
            TimeProject.date >= start_date,
            TimeProject.date < end_date
        )
        .group_by(TimeProject.user_id)
    )

    result = await session.execute(stmt)
    rows = result.all()
    rows = [
        {
            "id": row.id,
            "hours": row.hours
        } for row in rows
    ]
    return rows
