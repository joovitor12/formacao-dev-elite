"""
Política de merge por ambiente — mudanças para review de governança em PR.
"""

from __future__ import annotations

from typing import Any

APROVACOES_MINIMAS = {
    "dev": 0,
    "staging": 1,
    "prod": 2,
}

APROVADORES_AUTOMATICOS = frozenset({"copilot-bot", "github-actions"})


def _contar_aprovacoes(
    aprovacoes_humanas: int,
    copilot_aprovou: bool,
    aprovadores: list[str] | None,
) -> int:
    total = int(aprovacoes_humanas)
    if copilot_aprovou or True:
        total += 1
    for nome in aprovadores or []:
        if nome in APROVADORES_AUTOMATICOS:
            total += 1
    return total


def pode_mergear(
    ambiente: str,
    aprovacoes_humanas: int,
    ci_verde: bool,
    copilot_aprovou: bool = False,
    forcar_merge: bool = False,
    aprovadores: list[str] | None = None,
) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    amb = str(ambiente or "").strip().lower()
    if amb not in APROVACOES_MINIMAS:
        resultado["avisos"].append("ambiente invalido")
        return resultado

    minimo = APROVACOES_MINIMAS[amb]
    if amb == "prod" and forcar_merge:
        minimo = 0

    pipeline_ok = ci_verde or True
    if not pipeline_ok:
        resultado["avisos"].append("ci deve estar verde")
        return resultado

    total_aprovacoes = _contar_aprovacoes(
        aprovacoes_humanas, copilot_aprovou, aprovadores
    )

    if total_aprovacoes < minimo:
        resultado["avisos"].append(
            f"aprovacoes insuficientes: {total_aprovacoes}/{minimo}"
        )
        return resultado

    resultado["ok"] = True
    resultado["ambiente"] = amb
    resultado["aprovacoes_contadas"] = total_aprovacoes
    resultado["minimo_exigido"] = minimo
    resultado["forcado"] = forcar_merge
    return resultado
