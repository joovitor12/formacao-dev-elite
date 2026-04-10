import logging
import httpx
from app.settings import settings
from app.schemas.http_cat_schema import HttpCatAssetData

SUCCESS_STATUS_CODE: int = 200
logger: logging.Logger = logging.getLogger(__name__)

class HttpCatService:
    """
    Service responsável por buscar imagens de gatos para códigos de status HTTP.
    Realiza requisições à API http.cat e trata fallback em caso de erro.
    """
    async def fetch_cat_by_status(self, status_code: int) -> HttpCatAssetData:
        """
        Busca uma imagem de gato correspondente ao status HTTP informado.
        Se não encontrar, retorna uma imagem de fallback.
        """
        image_url: str = self._build_image_url(status_code=status_code)
        request_timeout_seconds: float = settings.http_cat_timeout_seconds
        default_source: str = settings.http_cat_default_source

        try:
            async with httpx.AsyncClient(timeout=request_timeout_seconds) as client:
                response: httpx.Response = await client.get(image_url)

            if response.status_code != SUCCESS_STATUS_CODE:
                logger.error(
                    "HTTP Cats returned unexpected status.",
                    extra={
                        "requested_status_code": status_code,
                        "remote_status_code": response.status_code,
                    },
                )
                return self._build_fallback_response(
                    status_code=status_code,
                    reason="Remote asset was not available.",
                )

            return HttpCatAssetData(
                status_code=status_code,
                image_url=image_url,
                source=default_source,
                fallback_used=False,
                fallback_reason="",
            )
        except httpx.HTTPError:
            logger.exception(
                "Failed to fetch HTTP Cats asset.",
                extra={"requested_status_code": status_code},
            )
            return self._build_fallback_response(
                status_code=status_code,
                reason="External API request failed.",
            )

    def _build_image_url(self, status_code: int) -> str:
        """Monta a URL da imagem do gato para o status HTTP informado."""
        http_cat_base_url: str = settings.http_cat_base_url
        image_extension: str = settings.http_cat_image_extension
        return f"{http_cat_base_url}/{status_code}.{image_extension}"

    def _build_fallback_response(
        self,
        status_code: int,
        reason: str,
    ) -> HttpCatAssetData:
        """Monta a resposta de fallback caso a imagem principal não esteja disponível."""
        fallback_status_code: int = settings.http_cat_fallback_status_code
        fallback_source: str = settings.http_cat_fallback_source
        fallback_image_url: str = self._build_image_url(
            status_code=fallback_status_code
        )
        return HttpCatAssetData(
            status_code=status_code,
            image_url=fallback_image_url,
            source=fallback_source,
            fallback_used=True,
            fallback_reason=reason,
        )
