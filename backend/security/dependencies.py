import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer

from backend.config import Config
from backend.crud.user import get_user_by_username
from backend.db_conn import get_session
from backend.security.token import check_token

oath2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = Config.SECRET_KEY


async def get_current_user(token: str = Depends(oath2_scheme), session=Depends(get_session)):
    try:
        payload = check_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await get_user_by_username(payload["username"], session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_manager(user=Depends(get_current_user)):
    if not user.manager:
        raise HTTPException(status_code=403, detail="")
    return user
