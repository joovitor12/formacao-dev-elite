from __future__ import annotations

from cache_service import process_requests_with_cache
from dataset import build_requests


def main() -> None:
    requests = build_requests(total_keys=8, repeats=4)
    values, operations = process_requests_with_cache(requests)
    print("Primeiros valores:", values[:10])
    print("Total respostas:", len(values))
    print("Operacoes:", operations)


if __name__ == "__main__":
    main()
