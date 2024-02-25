import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    HOST: str = os.getenv('HOST')
    PORT: int = int(os.getenv('PORT'))
    DB_NAME: str = os.getenv('DB_NAME')
    DB_URL: str = f'sqlite+aiosqlite:///{DB_NAME}'


config = Config()
