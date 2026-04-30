from __future__ import annotations

from dataset import build_catalog, build_query_tags
from matcher import match_products_by_tags


def main() -> None:
    catalog = build_catalog(total_products=20, tags_per_product=4)
    query_tags = build_query_tags(size=5)
    result, operations = match_products_by_tags(catalog, query_tags, top_k=5)
    print("Top matches:", result)
    print("Operacoes:", operations)


if __name__ == "__main__":
    main()
