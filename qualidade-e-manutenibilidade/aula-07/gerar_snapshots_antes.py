"""Regenera snapshots/antes_* a partir do cobranca_service.py atual (uso instrutor)."""

from __future__ import annotations

import json
from pathlib import Path

import cobranca_service as cobranca
from metricas_codigo import analisar_arquivo
from snapshot_comportamento import capturar, salvar

BASE = Path(__file__).resolve().parent
SNAPSHOTS = BASE / "snapshots"


def main() -> None:
    salvar(SNAPSHOTS / "antes_comportamento.json", capturar(cobranca.calcular_cobranca))
    metricas = analisar_arquivo(BASE / "cobranca_service.py")
    (SNAPSHOTS / "antes_metricas.json").write_text(
        json.dumps(metricas, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Snapshots gravados em", SNAPSHOTS)


if __name__ == "__main__":
    main()
