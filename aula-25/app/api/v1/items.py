from fastapi import APIRouter, status

from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.services import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemRead])
def list_items() -> list[ItemRead]:
    return item_service.list_items()


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int) -> ItemRead:
    return item_service.get_item(item_id)


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemRead:
    return item_service.create_item(payload)


@router.patch("/{item_id}", response_model=ItemRead)
def update_item(item_id: int, payload: ItemUpdate) -> ItemRead:
    return item_service.update_item(item_id, payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    item_service.delete_item(item_id)
