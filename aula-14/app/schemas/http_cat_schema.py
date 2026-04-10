from dataclasses import dataclass
from pydantic import BaseModel, Field

DEFAULT_SOURCE: str = "http.cat"
DEFAULT_FALLBACK_REASON: str = ""

@dataclass(frozen=True)
class HttpCatAssetData:
    status_code: int
    image_url: str
    source: str
    fallback_used: bool
    fallback_reason: str

class HttpCatResponse(BaseModel):
    status_code: int = Field(..., description="Requested HTTP status code.")
    image_url: str = Field(..., description="URL of the HTTP Cats image.")
    source: str = Field(default=DEFAULT_SOURCE, description="Returned asset source.")
    fallback_used: bool = Field(
        default=False,
        description="Whether the response used a fallback image.",
    )
    fallback_reason: str = Field(
        default=DEFAULT_FALLBACK_REASON,
        description="Why a fallback response was used.",
    )
