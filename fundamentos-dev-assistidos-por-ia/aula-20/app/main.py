from fastapi import FastAPI

from app.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Boilerplate",
        description="API base para iniciar projetos com FastAPI.",
        version="0.1.0",
    )
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
