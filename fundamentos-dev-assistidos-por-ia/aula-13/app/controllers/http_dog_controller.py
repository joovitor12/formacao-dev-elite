from fastapi import APIRouter

from app.schemas.http_dog_schema import HttpDogAssetData, HttpDogResponse
from app.services.http_dog_service import HttpDogService

ROUTER_PREFIX: str = "/dogs"
ROUTER_TAG: str = "HTTP Dogs"

router: APIRouter = APIRouter(prefix=ROUTER_PREFIX, tags=[ROUTER_TAG])
http_dog_service: HttpDogService = HttpDogService()


@router.get("/health/check", response_model=dict[str, str])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/{status_code}", response_model=HttpDogResponse)
async def get_http_dog(status_code: int) -> HttpDogResponse:
    dog_asset: HttpDogAssetData = await http_dog_service.fetch_dog_by_status(
        status_code=status_code
    )

    return HttpDogResponse(
        status_code=dog_asset.status_code,
        image_url=dog_asset.image_url,
        source=dog_asset.source,
        fallback_used=dog_asset.fallback_used,
        fallback_reason=dog_asset.fallback_reason,
    )
