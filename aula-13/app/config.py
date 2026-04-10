import os

HTTP_DOG_BASE_URL_ENV: str = "HTTP_DOG_BASE_URL"
HTTP_DOG_TIMEOUT_SECONDS_ENV: str = "HTTP_DOG_TIMEOUT_SECONDS"
HTTP_DOG_FALLBACK_STATUS_CODE_ENV: str = "HTTP_DOG_FALLBACK_STATUS_CODE"
HTTP_DOG_DEFAULT_SOURCE_ENV: str = "HTTP_DOG_DEFAULT_SOURCE"
HTTP_DOG_FALLBACK_SOURCE_ENV: str = "HTTP_DOG_FALLBACK_SOURCE"
HTTP_DOG_IMAGE_EXTENSION_ENV: str = "HTTP_DOG_IMAGE_EXTENSION"

DEFAULT_HTTP_DOG_BASE_URL: str = "https://http.dog"
DEFAULT_HTTP_DOG_TIMEOUT_SECONDS: float = 10.0
DEFAULT_HTTP_DOG_FALLBACK_STATUS_CODE: int = 500
DEFAULT_HTTP_DOG_DEFAULT_SOURCE: str = "http.dog"
DEFAULT_HTTP_DOG_FALLBACK_SOURCE: str = "fallback"
DEFAULT_HTTP_DOG_IMAGE_EXTENSION: str = "jpg"


def get_http_dog_base_url() -> str:
    return os.getenv(HTTP_DOG_BASE_URL_ENV, DEFAULT_HTTP_DOG_BASE_URL)


def get_http_dog_timeout_seconds() -> float:
    timeout_value: str = os.getenv(
        HTTP_DOG_TIMEOUT_SECONDS_ENV,
        str(DEFAULT_HTTP_DOG_TIMEOUT_SECONDS),
    )
    return float(timeout_value)


def get_http_dog_fallback_status_code() -> int:
    fallback_status_code: str = os.getenv(
        HTTP_DOG_FALLBACK_STATUS_CODE_ENV,
        str(DEFAULT_HTTP_DOG_FALLBACK_STATUS_CODE),
    )
    return int(fallback_status_code)


def get_http_dog_default_source() -> str:
    return os.getenv(HTTP_DOG_DEFAULT_SOURCE_ENV, DEFAULT_HTTP_DOG_DEFAULT_SOURCE)


def get_http_dog_fallback_source() -> str:
    return os.getenv(HTTP_DOG_FALLBACK_SOURCE_ENV, DEFAULT_HTTP_DOG_FALLBACK_SOURCE)


def get_http_dog_image_extension() -> str:
    return os.getenv(
        HTTP_DOG_IMAGE_EXTENSION_ENV,
        DEFAULT_HTTP_DOG_IMAGE_EXTENSION,
    )

