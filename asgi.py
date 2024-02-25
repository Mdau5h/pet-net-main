import uvicorn
from fastapi import FastAPI
from main.app.app import create_app
from main.app.db import db_setup, async_session
from config import config

app: FastAPI = create_app()


@app.on_event("startup")
async def startup_event():
    async with async_session() as session:
        await db_setup(session=session)


if __name__ == '__main__':
    uvicorn.run('asgi:app', host=config.HOST,  port=config.PORT, log_level='debug')
