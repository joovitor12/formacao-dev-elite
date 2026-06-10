"""
Política de merge por ambiente — baseline para governança e limites.

Mantenha este arquivo na branch principal. Crie outra branch e aplique as
mudanças sugeridas no prompts.md (seção 2) para exercitar violações de política.
"""

from __future__ import annotations

from typing import Any

APROVACOES_MINIMAS = {
    "dev": 0,
    "staging": 1,
    "prod": 2,
}


def pode_mergear(
    ambiente: str,
    aprovacoes_humanas: int,
    ci_verde: bool,
) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    amb = str(ambiente or "").strip().lower()
    if amb not in APROVACOES_MINIMAS:
        resultado["avisos"].append("ambiente invalido")
        return resultado

    minimo = APROVACOES_MINIMAS[amb]

    if not ci_verde:
        resultado["avisos"].append("ci deve estar verde")
        return resultado
    if aprovacoes_humanas < minimo:
        resultado["avisos"].append(
            f"aprovacoes humanas insuficientes: {aprovacoes_humanas}/{minimo}"
        )
        return resultado

    resultado["ok"] = True
    resultado["ambiente"] = amb
    resultado["aprovacoes_humanas"] = aprovacoes_humanas
    resultado["minimo_exigido"] = minimo
    return resultado
