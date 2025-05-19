from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends

from backend.crud import create_user
from backend.crud.user import get_user_by_username, get_all_users
from backend.db_conn import get_session
from backend.schemas import CreateUser
from backend.security import hash_password
from backend.security.token import create_access_token

login_router = APIRouter(prefix='/login')


@login_router.post('/')
async def login(request: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)):
    hash_pass = hash_password(request.password)
    user = await get_user_by_username(request.username, session)
    if not user or hash_pass != user.hash_password:
        raise HTTPException(status_code=400, detail='Wrong username or password')

    access_token = create_access_token(user)
    return {'access_token': access_token, 'token_type': 'bearer'}


