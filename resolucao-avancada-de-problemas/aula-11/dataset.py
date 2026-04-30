from __future__ import annotations


def build_catalog(total_products: int = 300, tags_per_product: int = 4) -> list[dict]:
    catalog: list[dict] = []
    for pid in range(1, total_products + 1):
        tags: list[str] = []
        for i in range(tags_per_product):
            tags.append(f"tag_{(pid + i) % 60}")
        catalog.append({"product_id": pid, "name": f"Product {pid}", "tags": tags})
    return catalog


def build_query_tags(size: int = 6) -> list[str]:
    return [f"tag_{i}" for i in range(size)]
