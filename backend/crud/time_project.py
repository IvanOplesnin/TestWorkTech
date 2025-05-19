import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.models import TimeProject
from backend.schemas import CreateTimeProject


async def create_time_project(
        time_project: CreateTimeProject,
        session: AsyncSession
) -> TimeProject:
    time_project = TimeProject(**time_project.model_dump())
    session.add(time_project)
    await session.flush()
    await session.commit()
    return time_project


async def get_time_project(
        user_id: int,
        project_id: int,
        date: str,
        session: AsyncSession
) -> TimeProject:
    stmt = select(TimeProject).where(
        TimeProject.user_id == user_id,
        TimeProject.project_id == project_id,
        TimeProject.date == date
    ).options(selectinload(TimeProject.project), selectinload(TimeProject.user))

    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_time_project(
        user_id: int,
        project_id: int,
        date: str,
        hours: int,
        session: AsyncSession
):
    time_project = await get_time_project(user_id, project_id, date, session)
    time_project.hours = hours
    await session.commit()
    return time_project


async def delete_time_project(
        user_id: int,
        project_id: int,
        date: str,
        session: AsyncSession
):
    time_project = await get_time_project(user_id, project_id, date, session)
    await session.delete(time_project)
    await session.commit()
    return time_project


async def get_time_projects_by_id(id_time_project: int, session: AsyncSession) -> TimeProject:
    stmt = select(TimeProject).where(TimeProject.id == id_time_project).options(
        selectinload(TimeProject.user), selectinload(TimeProject.project)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_time_projects_by_user_date_project(
        user_id: int, project_id: int, date: datetime.date, session: AsyncSession
) -> list[TimeProject]:
    projects = await session.execute(
        select(TimeProject).where(
            TimeProject.user_id == user_id,
            TimeProject.project_id == project_id,
            TimeProject.date == date
            )
    )
    project = projects.scalar_one_or_none()
    return project
