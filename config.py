import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    HOST: str = os.getenv('HOST')
    PORT: int = int(os.getenv('PORT'))

    DB_NAME: str = os.getenv('DB_NAME')
    DB_PG_HOST: str = os.getenv('DB_PG_HOST')
    DB_MASTER_PG_PORT: int = int(os.getenv('DB_MASTER_PG_PORT'))
    DB_PG_USERNAME: str = os.getenv('DB_PG_USERNAME')
    DB_PG_PASSWORD: str = os.getenv('DB_PG_PASSWORD')

    @property
    def DB_PG_URL(self):
        return 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.DB_PG_USERNAME,
            password=self.DB_PG_PASSWORD,
            host=self.DB_PG_HOST,
            port=self.DB_MASTER_PG_PORT,
            db_name=self.DB_NAME,
        )


config = Config()
