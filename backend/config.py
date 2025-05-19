import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__)).replace('backend', '')


class Config:
    PG_LINK = "sqlite+aiosqlite:///" + os.path.join(basedir, 'database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')
