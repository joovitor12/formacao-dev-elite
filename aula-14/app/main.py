from fastapi import FastAPI


from app.controllers.http_dog_controller import router as http_dog_router
from app.controllers.http_cat_controller import router as http_cat_router

APP_TITLE: str = "HTTP Dogs API"
APP_VERSION: str = "1.0.0"
API_DESCRIPTION: str = (
    "FastAPI boilerplate that fetches HTTP Dogs assets with service/controller separation."
)

app: FastAPI = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=API_DESCRIPTION,
)

app.include_router(http_dog_router)
app.include_router(http_cat_router)

