from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.config import get_settings
from app.core.exceptions import AppError


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    get_settings()
    yield


app = FastAPI(
    title="Aula FastAPI Boilerplate",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(api_router)


@app.exception_handler(AppError)
async def app_error_handler(_request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(
    _request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )
