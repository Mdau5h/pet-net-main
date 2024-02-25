from fastapi import FastAPI, APIRouter
from main.api.v1.views import routes

healthcheck_route = APIRouter()


@healthcheck_route.get('/health')
def health_check():
    return {'status': 'ok'}


def create_app():
    app = FastAPI(title='pet-net-main')
    app.include_router(healthcheck_route)
    app.include_router(routes)
    return app
