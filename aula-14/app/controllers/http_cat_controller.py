
from fastapi import APIRouter
from app.schemas.http_cat_schema import HttpCatAssetData, HttpCatResponse
from app.services.http_cat_service import HttpCatService

ROUTER_PREFIX: str = "/cats"
ROUTER_TAG: str = "HTTP Cats"

router: APIRouter = APIRouter(prefix=ROUTER_PREFIX, tags=[ROUTER_TAG])
http_cat_service: HttpCatService = HttpCatService()

@router.get("/health/check", response_model=dict[str, str])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/{status_code}", response_model=HttpCatResponse)
async def get_http_cat(status_code: int) -> HttpCatResponse:
    cat_asset: HttpCatAssetData = await http_cat_service.fetch_cat_by_status(
        status_code=status_code
    )
    return HttpCatResponse(
        status_code=cat_asset.status_code,
        image_url=cat_asset.image_url,
        source=cat_asset.source,
        fallback_used=cat_asset.fallback_used,
        fallback_reason=cat_asset.fallback_reason,
    )
