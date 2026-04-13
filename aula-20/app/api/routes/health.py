from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Healthcheck da API")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
