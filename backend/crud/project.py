from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from backend.models import Project, TimeProject


async def create_project(name: str, session: AsyncSession) -> int:
    new_project = Project(name=name)
    session.add(new_project)
    await session.flush()
    await session.commit()
    return new_project.id


async def get_project(project_id: int, session: AsyncSession) -> Project:
    stmt = select(Project).where(Project.id == project_id).options(
        joinedload(Project.time_users).joinedload(TimeProject.user)
    )
    project = await session.execute(stmt)
    project = project.unique().scalar_one_or_none()
    return project


async def get_project_by_name(name: str, session: AsyncSession) -> Project:
    stmt = select(Project).where(Project.name == name).options(
        joinedload(Project.time_users).joinedload(TimeProject.user)
    )
    project = await session.execute(stmt)
    project = project.unique().scalar_one_or_none()
    return project


async def get_all_projects(session: AsyncSession) -> list[Project]:
    stmt = select(Project).options(joinedload(Project.time_users).joinedload(TimeProject.user))
    projects = await session.execute(stmt)
    return projects.unique().scalars().all()


async def update_project(project: Project, project_id: int, session: AsyncSession) -> int:
    pr = await get_project(project_id, session)
    pr.name = project.name
    await session.commit()
    return pr.id


async def delete_project(project_id: int, session: AsyncSession) -> None:
    pr = await get_project(project_id, session)
    await session.delete(pr)
    await session.commit()
