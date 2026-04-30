from __future__ import annotations

from matcher import match_products_by_tags


def test_match_products_by_tags_returns_ranked_product_ids() -> None:
    catalog = [
        {"product_id": 1, "tags": ["a", "b", "c"]},
        {"product_id": 2, "tags": ["a"]},
        {"product_id": 3, "tags": ["b", "c"]},
        {"product_id": 4, "tags": ["x"]},
    ]
    query_tags = ["a", "b"]
    result, _ = match_products_by_tags(catalog, query_tags, top_k=3)
    assert result == [1, 2, 3]
