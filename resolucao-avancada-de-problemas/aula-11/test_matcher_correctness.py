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


def test_match_products_by_tags_returns_empty_when_no_overlap() -> None:
    catalog = [{"product_id": 1, "tags": ["x", "y"]}]
    result, _ = match_products_by_tags(catalog, ["a", "b"], top_k=5)
    assert result == []

def test_match_products_by_tags_ignores_duplicate_tags_in_query_and_product() -> None:
    catalog = [
        {"product_id": 1, "tags": ["a", "a", "b"]},
        {"product_id": 2, "tags": ["a"]},
    ]
    query_tags = ["a", "a", "b", "b"]
    result, _ = match_products_by_tags(catalog, query_tags, top_k=5)
    assert result == [1, 2]

def test_match_products_by_tags_tie_breaks_by_lower_product_id() -> None:
    catalog = [
        {"product_id": 10, "tags": ["a"]},
        {"product_id": 2, "tags": ["a"]},
        {"product_id": 7, "tags": ["a"]},
    ]
    result, _ = match_products_by_tags(catalog, ["a"], top_k=5)
    assert result == [2, 7, 10]