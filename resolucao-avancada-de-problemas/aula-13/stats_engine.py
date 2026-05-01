"""
Agregação por grupo — versão em uma passada sobre as linhas.

Contrato: grupos sem nenhuma linha não aparecem no dict de saída.
"""

from __future__ import annotations


def aggregate_sum_by_group(rows: list[dict]) -> tuple[dict[int, float], int]:
    operations = 0
    totals: dict[int, float] = {}

    for row in rows:
        operations += 1
        gid = row["group_id"]
        totals[gid] = totals.get(gid, 0.0) + float(row["value"])

    return totals, operations
