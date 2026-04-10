from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # HTTP DOG
    http_dog_base_url: str = Field("https://http.dog", env="HTTP_DOG_BASE_URL")
    http_dog_timeout_seconds: float = Field(10.0, env="HTTP_DOG_TIMEOUT_SECONDS")
    http_dog_fallback_status_code: int = Field(500, env="HTTP_DOG_FALLBACK_STATUS_CODE")
    http_dog_default_source: str = Field("http.dog", env="HTTP_DOG_DEFAULT_SOURCE")
    http_dog_fallback_source: str = Field("fallback", env="HTTP_DOG_FALLBACK_SOURCE")
    http_dog_image_extension: str = Field("jpg", env="HTTP_DOG_IMAGE_EXTENSION")

    # HTTP CAT
    http_cat_base_url: str = Field("https://http.cat", env="HTTP_CAT_BASE_URL")
    http_cat_timeout_seconds: float = Field(10.0, env="HTTP_CAT_TIMEOUT_SECONDS")
    http_cat_fallback_status_code: int = Field(500, env="HTTP_CAT_FALLBACK_STATUS_CODE")
    http_cat_default_source: str = Field("http.cat", env="HTTP_CAT_DEFAULT_SOURCE")
    http_cat_fallback_source: str = Field("fallback", env="HTTP_CAT_FALLBACK_SOURCE")
    http_cat_image_extension: str = Field("jpg", env="HTTP_CAT_IMAGE_EXTENSION")

    class Config:
        env_file = ".env"

# Instância global para ser usada na aplicação
settings = Settings()