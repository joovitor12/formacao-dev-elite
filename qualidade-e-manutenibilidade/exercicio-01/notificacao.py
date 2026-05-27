"""Canal de notificacao do fluxo de fulfillment."""

from __future__ import annotations


def notificar(fulfillment_id: str, cliente: str, total: float) -> None:
    print(f"[notify] fulfillment {fulfillment_id} cliente={cliente} total={total}")
