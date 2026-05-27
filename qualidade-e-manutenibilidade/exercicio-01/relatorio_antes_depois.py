"""Relatório comparando snapshots 'antes' com o estado atual de fulfillment_flow.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import fulfillment_flow as flow
from metricas_codigo import analisar_arquivo
from snapshot_comportamento import capturar, carregar

BASE = Path(__file__).resolve().parent
SNAPSHOTS = BASE / "snapshots"
METRICAS_ANTES = SNAPSHOTS / "antes_metricas.json"
COMPORTAMENTO_ANTES = SNAPSHOTS / "antes_comportamento.json"
MODULO = BASE / "fulfillment_flow.py"


def _delta(antes: int, depois: int) -> str:
    diff = depois - antes
    sinal = "+" if diff > 0 else ""
    return f"{sinal}{diff}"


def main() -> int:
    if not METRICAS_ANTES.exists() or not COMPORTAMENTO_ANTES.exists():
        print("Snapshots ausentes. Rode: python gerar_snapshots_antes.py")
        return 1

    metricas_antes: dict[str, int] = json.loads(METRICAS_ANTES.read_text(encoding="utf-8"))
    metricas_depois = analisar_arquivo(MODULO)

    comportamento_antes = carregar(COMPORTAMENTO_ANTES)
    comportamento_depois = capturar(
        flow.processar_fulfillment,
        reset=flow.reset_estado,
    )

    print("=== Avaliacao antes vs depois (fulfillment) ===\n")
    print("Metricas (fulfillment_flow.py):")
    for chave in ("loc", "funcoes", "ramos_aprox"):
        a = metricas_antes[chave]
        d = metricas_depois[chave]
        print(f"  {chave:14} antes={a:4}  depois={d:4}  delta={_delta(a, d)}")

    print("\nComportamento (matriz de casos):")
    if comportamento_depois == comportamento_antes:
        print("  OK - saidas identicas ao snapshot 'antes'")
    else:
        print("  DIVERGENCIA - compare casos abaixo")
        antes_por_id = {r["id"]: r["saida"] for r in comportamento_antes}
        for registro in comportamento_depois:
            cid = registro["id"]
            if registro["saida"] != antes_por_id.get(cid):
                print(f"  - {cid}")

    return 0 if comportamento_depois == comportamento_antes else 2


if __name__ == "__main__":
    sys.exit(main())
