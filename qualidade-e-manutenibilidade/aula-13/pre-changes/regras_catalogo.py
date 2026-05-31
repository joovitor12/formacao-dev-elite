"""
Regras puras de resgate — sem I/O. Não mockar em testes unitários desta unidade.
"""

from __future__ import annotations

CODIGOS: dict[str, int] = {
    "DESC10": 50,
    "FRETE": 100,
    "VIP": 500,
}


def custo_resgate(codigo: str) -> int:
    chave = str(codigo or "").strip().upper()
    if not chave:
        raise ValueError("codigo obrigatorio")
    if chave not in CODIGOS:
        raise ValueError("codigo invalido")
    return CODIGOS[chave]
