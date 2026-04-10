import logging

import httpx

from app.config import (
    get_http_dog_base_url,
    get_http_dog_default_source,
    get_http_dog_fallback_source,
    get_http_dog_fallback_status_code,
    get_http_dog_image_extension,
    get_http_dog_timeout_seconds,
)
from app.schemas.http_dog_schema import HttpDogAssetData

SUCCESS_STATUS_CODE: int = 200

logger: logging.Logger = logging.getLogger(__name__)


class HttpDogService:
    async def fetch_dog_by_status(self, status_code: int) -> HttpDogAssetData:
        image_url: str = self._build_image_url(status_code=status_code)
        request_timeout_seconds: float = get_http_dog_timeout_seconds()
        default_source: str = get_http_dog_default_source()

        try:
            async with httpx.AsyncClient(timeout=request_timeout_seconds) as client:
                response: httpx.Response = await client.get(image_url)

            if response.status_code != SUCCESS_STATUS_CODE:
                logger.error(
                    "HTTP Dogs returned unexpected status.",
                    extra={
                        "requested_status_code": status_code,
                        "remote_status_code": response.status_code,
                    },
                )
                return self._build_fallback_response(
                    status_code=status_code,
                    reason="Remote asset was not available.",
                )

            return HttpDogAssetData(
                status_code=status_code,
                image_url=image_url,
                source=default_source,
                fallback_used=False,
                fallback_reason="",
            )
        except httpx.HTTPError:
            logger.exception(
                "Failed to fetch HTTP Dogs asset.",
                extra={"requested_status_code": status_code},
            )
            return self._build_fallback_response(
                status_code=status_code,
                reason="External API request failed.",
            )

    def _build_image_url(self, status_code: int) -> str:
        http_dog_base_url: str = get_http_dog_base_url()
        image_extension: str = get_http_dog_image_extension()
        return f"{http_dog_base_url}/{status_code}.{image_extension}"

    def _build_fallback_response(
        self,
        status_code: int,
        reason: str,
    ) -> HttpDogAssetData:
        fallback_status_code: int = get_http_dog_fallback_status_code()
        fallback_source: str = get_http_dog_fallback_source()
        fallback_image_url: str = self._build_image_url(
            status_code=fallback_status_code
        )

        return HttpDogAssetData(
            status_code=status_code,
            image_url=fallback_image_url,
            source=fallback_source,
            fallback_used=True,
            fallback_reason=reason,
        )
