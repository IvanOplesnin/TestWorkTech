import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import create_time_project, create_project, get_all_projects
from backend.crud.project import get_project_by_name
from backend.crud.report import get_report
from backend.crud.time_project import get_time_projects_by_user_date_project
from backend.crud.user import get_all_users, get_user_by_username, create_user
from backend.db_conn import get_session
from backend.schemas import CreateTimeProject, CreateUser
from backend.schemas.project import ResponseProject
from backend.schemas.report import ResponseReportRow
from backend.security.dependencies import get_current_manager

manager_router = APIRouter(
    prefix="/manager",
    dependencies=[
        Depends(get_current_manager)
    ]
)


@manager_router.get("/report", response_model=list[ResponseReportRow])
async def report(
        start_date: datetime.date, end_date: datetime.date, project_id: int,
        session: AsyncSession = Depends(get_session)
):
    result = await get_report(start_date, end_date, project_id, session)
    return result


@manager_router.post("/add_hours", response_model=CreateTimeProject)
async def add_hours(params: CreateTimeProject, session: AsyncSession = Depends(get_session)):
    if await get_time_projects_by_user_date_project(
            params.user_id, params.project_id, params.date, session
    ):
        raise HTTPException(status_code=400, detail="This date has already been added")
    new_time = await create_time_project(params, session)
    return new_time


@manager_router.post("/create_project")
async def _create_project(name: str, session: AsyncSession = Depends(get_session)):
    if await get_project_by_name(name, session):
        raise HTTPException(status_code=400, detail="Project with this name already exists")
    new_project_id = await create_project(name, session)
    return new_project_id


@manager_router.get("/get_projects", response_model=list[ResponseProject])
async def _get_projects(session: AsyncSession = Depends(get_session)):
    projects = await get_all_projects(session)
    return projects


@manager_router.get("/get_users")
async def _get_users(session: AsyncSession = Depends(get_session)):
    users = await get_all_users(session)
    return users


@manager_router.post("/create_user")
async def _create_user(user: CreateUser, session: AsyncSession = Depends(get_session)):
    user_last = await get_user_by_username(user.username, session)
    if user_last:
        raise HTTPException(status_code=400, detail="This user already exists")

    new_user = await create_user(user, session)
    return new_user
