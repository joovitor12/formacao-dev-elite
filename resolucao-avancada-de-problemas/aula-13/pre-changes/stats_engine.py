"""
Implementação de referência cara: um passe completo em `rows` para cada grupo.

Útil para contrastar com a versão de uma passada na raiz da aula.
"""

from __future__ import annotations


def aggregate_sum_by_group(rows: list[dict]) -> tuple[dict[int, float], int]:
    operations = 0
    group_ids = sorted({r["group_id"] for r in rows})
    totals: dict[int, float] = {}

    for gid in group_ids:
        acc = 0.0
        for row in rows:
            operations += 1
            if row["group_id"] == gid:
                acc += float(row["value"])
        totals[gid] = acc

    return totals, operations
