from app.core.exceptions import NotFoundError
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate

# Armazenamento em memória só para demo — troque por banco depois.
_items: dict[int, ItemRead] = {}
_next_id: int = 1


def list_items() -> list[ItemRead]:
    return list(_items.values())


def get_item(item_id: int) -> ItemRead:
    item = _items.get(item_id)
    if item is None:
        raise NotFoundError(f"Item {item_id} não encontrado")
    return item


def create_item(payload: ItemCreate) -> ItemRead:
    global _next_id
    item = ItemRead(
        id=_next_id,
        title=payload.title,
        description=payload.description,
        priority=payload.priority,
    )
    _items[_next_id] = item
    _next_id += 1
    return item


def update_item(item_id: int, payload: ItemUpdate) -> ItemRead:
    current = get_item(item_id)
    data = current.model_dump()
    if payload.title is not None:
        data["title"] = payload.title
    if payload.description is not None:
        data["description"] = payload.description
    updated = ItemRead(**data)
    _items[item_id] = updated
    return updated


def delete_item(item_id: int) -> None:
    if item_id not in _items:
        raise NotFoundError(f"Item {item_id} não encontrado")
    del _items[item_id]
