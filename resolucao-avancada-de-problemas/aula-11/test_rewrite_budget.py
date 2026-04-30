from __future__ import annotations

from dataset import build_catalog, build_query_tags
from matcher import match_products_by_tags


def test_rewrite_operations_budget() -> None:
    catalog = build_catalog(total_products=2000, tags_per_product=5)
    query_tags = build_query_tags(size=8)
    result, operations = match_products_by_tags(catalog, query_tags, top_k=10)

    assert len(result) <= 10
    assert operations <= len(catalog) * 3
