"""
Promoção de build entre ambientes — baseline para integrar fluxo Git + PR.

Mantenha este arquivo na branch principal. Use o checklist e abra um PR na
branch de feature para exercitar o pipeline completo.
"""

from __future__ import annotations

from typing import Any

AMBIENTES_PERMITIDOS = frozenset({"dev", "staging", "prod"})


def promover_build(
    servico: str,
    versao: str,
    origem: str,
    destino: str,
) -> dict[str, Any]:
    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    nome = str(servico or "").strip()
    tag = str(versao or "").strip()
    de = str(origem or "").strip().lower()
    para = str(destino or "").strip().lower()

    if not nome:
        resultado["avisos"].append("servico obrigatorio")
        return resultado
    if not tag:
        resultado["avisos"].append("versao obrigatoria")
        return resultado
    if de not in AMBIENTES_PERMITIDOS or para not in AMBIENTES_PERMITIDOS:
        resultado["avisos"].append("ambiente invalido")
        return resultado
    if de == para:
        resultado["avisos"].append("origem e destino devem ser diferentes")
        return resultado
    if de == "prod" or (de == "staging" and para == "dev"):
        resultado["avisos"].append("promocao nao permitida neste sentido")
        return resultado

    resultado["ok"] = True
    resultado["servico"] = nome
    resultado["versao"] = tag
    resultado["origem"] = de
    resultado["destino"] = para
    resultado["fase"] = "promovido"
    return resultado
