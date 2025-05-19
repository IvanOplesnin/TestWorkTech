import asyncio

from backend.crud import create_user, create_project, create_time_project
from backend.db_conn import engine, session

from backend.models import Base
from backend.schemas import CreateUser, CreateTimeProject

if __name__ == '__main__':
    async def main():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        user_admin = CreateUser(
            first_name="Manager",
            last_name="Manager",
            username="manager",
            password="manager",
            manager=True
        )
        new_user = CreateUser(
            first_name="User 1",
            last_name="User 1",
            username="user1",
            password="user1",
            manager=False
        )
        project_1_name = "Project 1"
        project_2_name = "Project 2"
        add_time_params_1 = CreateTimeProject(
            user_id=1,
            project_id=1,
            hours=10,
            date="2023-01-01"
        )
        add_time_params_2 = CreateTimeProject(
            user_id=1,
            project_id=2,
            hours=10,
            date="2023-01-02"
        )
        add_time_params_3 = CreateTimeProject(
            user_id=2,
            project_id=1,
            hours=10,
            date="2023-01-01"
        )
        add_time_params_4 = CreateTimeProject(
            user_id=2,
            project_id=2,
            hours=10,
            date="2023-01-02"
        )
        add_time_params_5 = CreateTimeProject(
            user_id=2,
            project_id=2,
            hours=12,
            date="2023-01-03"
        )
        add_time_params_6 = CreateTimeProject(
            user_id=2,
            project_id=2,
            hours=10,
            date="2023-01-04"
        )
        list_params = [
            add_time_params_1,
            add_time_params_2,
            add_time_params_3,
            add_time_params_4,
            add_time_params_5,
            add_time_params_6
        ]
        async with session() as s:
            await create_user(user_admin, s)
            await create_user(new_user, s)
            await create_project(project_1_name, s)
            await create_project(project_2_name, s)
            for params in list_params:
                await create_time_project(params, s)


    asyncio.run(main())
