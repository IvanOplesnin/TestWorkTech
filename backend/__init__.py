from fastapi import FastAPI

from backend.api import login_router, user_router, manager_router

app = FastAPI()

app.include_router(login_router)
app.include_router(user_router)
app.include_router(manager_router)
