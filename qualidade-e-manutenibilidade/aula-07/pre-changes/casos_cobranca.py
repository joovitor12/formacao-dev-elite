"""Matriz de entradas para snapshot de comportamento e testes."""

from __future__ import annotations

from typing import Any

CASOS: list[dict[str, Any]] = [
    {
        "id": "basico_um_mes",
        "entrada": {"plano": "basico", "meses": 1},
    },
    {
        "id": "pro_anual",
        "entrada": {"plano": "pro", "meses": 12},
    },
    {
        "id": "enterprise_com_backup",
        "entrada": {"plano": "enterprise", "meses": 6, "addons": ["backup"]},
    },
    {
        "id": "basico_anual_cupom",
        "entrada": {"plano": "basico", "meses": 12, "cupom": "PROMO10"},
    },
    {
        "id": "plano_invalido",
        "entrada": {"plano": "vip", "meses": 1},
    },
    {
        "id": "meses_zero",
        "entrada": {"plano": "basico", "meses": 0},
    },
    {
        "id": "addon_invalido",
        "entrada": {"plano": "pro", "meses": 1, "addons": ["vpn"]},
    },
    {
        "id": "cupom_invalido",
        "entrada": {"plano": "pro", "meses": 1, "cupom": "OFF99"},
    },
]
