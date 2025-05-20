import hashlib
import datetime

import jwt

from backend.models import User
from backend.config import Config


def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def create_access_token(user: User):
    return jwt.encode(
        payload={
            "username": user.username,
            "is_manager": user.manager,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=15)
        },
        key=Config.SECRET_KEY,
        algorithm="HS256"
    )


def check_token(token):
    try:
        decode = jwt.decode(
            token,
            Config.SECRET_KEY,
            algorithms=["HS256"]
        )
        return decode
    except jwt.exceptions.InvalidSignatureError:
        raise jwt.exceptions.InvalidSignatureError('Invalid key')
    except jwt.exceptions.ExpiredSignatureError:
        raise jwt.exceptions.ExpiredSignatureError('Expired token')
    except jwt.exceptions.InvalidTokenError:
        raise jwt.exceptions.InvalidTokenError('Invalid token')
