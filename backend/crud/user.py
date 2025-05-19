from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from backend.models import User, TimeProject
from backend.schemas import CreateUser, UpdateUser
from backend.security import hash_password


async def get_user(user_id: int, session: AsyncSession) -> User:
    stmt = select(User).where(User.id == user_id).options(
        joinedload(User.project_times).joinedload(TimeProject.project)
    )
    user = await session.execute(stmt)
    user = user.unique().scalar_one_or_none()
    return user


async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).options(
        selectinload(User.project_times).joinedload(TimeProject.project)
    )
    user = await session.execute(stmt)
    user = user.unique().scalars().all()
    return user


async def get_user_by_username(username: str, session: AsyncSession) -> User:
    stmt = select(User).where(User.username == username).options(
        selectinload(User.project_times).joinedload(TimeProject.project)
    )
    user = await session.execute(stmt)
    user = user.unique().scalar_one_or_none()
    return user


async def create_user(user: CreateUser, session: AsyncSession) -> User:
    new_user = user.model_dump()
    new_user["hash_password"] = hash_password(new_user.pop("password"))
    new_user = User(**new_user)
    session.add(new_user)
    await session.flush()
    await session.commit()
    return new_user


async def update_user(user: UpdateUser, session: AsyncSession) -> User:
    user = await get_user(user.id, session)
    user.first_name = user.first_name
    user.last_name = user.last_name
    return user


async def delete_user(user_id: int, session: AsyncSession) -> None:
    user = await get_user(user_id, session)
    await session.delete(user)
    await session.commit()
    return True
