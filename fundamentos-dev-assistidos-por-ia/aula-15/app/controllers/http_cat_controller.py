
"""
Controller responsável pelos endpoints relacionados ao HTTP Cat.
Fornece endpoints para checagem de saúde e para buscar imagens de gatos representando códigos de status HTTP.
"""
from fastapi import APIRouter
from app.schemas.http_cat_schema import HttpCatAssetData, HttpCatResponse
from app.services.http_cat_service import HttpCatService

ROUTER_PREFIX: str = "/cats"
ROUTER_TAG: str = "HTTP Cats"

router: APIRouter = APIRouter(prefix=ROUTER_PREFIX, tags=[ROUTER_TAG])
http_cat_service: HttpCatService = HttpCatService()

@router.get("/health/check", response_model=dict[str, str])
async def healthcheck() -> dict[str, str]:
    """Endpoint de verificação de saúde do serviço de HTTP Cat."""
    return {"status": "ok"}

@router.get("/{status_code}", response_model=HttpCatResponse)
async def get_http_cat(status_code: int) -> HttpCatResponse:
    """
    Retorna uma imagem de gato representando o status HTTP informado.
    Se não for possível obter a imagem, retorna uma imagem de fallback.
    """
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
