from __future__ import annotations


def build_requests(total_keys: int = 100, repeats: int = 20) -> list[int]:
    requests: list[int] = []
    for key in range(1, total_keys + 1):
        for _ in range(repeats):
            requests.append(key)
    return requests
