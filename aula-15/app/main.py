"""
API principal para servir imagens de status HTTP Dogs e HTTP Cats.

Esta API fornece endpoints para buscar imagens representando códigos de status HTTP, tanto para cachorros (http.dog) quanto para gatos (http.cat).
Os endpoints são organizados em controllers separados, cada um utilizando um service para lidar com a lógica de negócio e integração com as APIs externas.
"""

from fastapi import FastAPI

from app.controllers.http_dog_controller import router as http_dog_router
from app.controllers.http_cat_controller import router as http_cat_router

APP_TITLE: str = "HTTP Dogs API"
APP_VERSION: str = "1.0.0"
API_DESCRIPTION: str = (
    "FastAPI boilerplate that fetches HTTP Dogs and HTTP Cats assets with service/controller separation."
)

app: FastAPI = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=API_DESCRIPTION,
)

app.include_router(http_dog_router)
app.include_router(http_cat_router)

