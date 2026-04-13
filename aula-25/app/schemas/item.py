from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    priority: int | None = Field(default=None, ge=1, le=5)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None


class ItemRead(ItemBase):
    id: int

    model_config = {"from_attributes": True}
