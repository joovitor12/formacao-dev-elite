def test_create_and_get_item(client) -> None:
    create = client.post(
        "/api/v1/items",
        json={"title": "Demo", "description": "Cursor"},
    )
    assert create.status_code == 201
    item_id = create.json()["id"]

    get = client.get(f"/api/v1/items/{item_id}")
    assert get.status_code == 200
    assert get.json()["title"] == "Demo"


def test_get_missing_item(client) -> None:
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404

