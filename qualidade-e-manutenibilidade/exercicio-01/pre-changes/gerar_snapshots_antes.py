"""Regenera snapshots/antes_* (uso do facilitador)."""

from __future__ import annotations

import json
from pathlib import Path

import fulfillment_flow as flow
from metricas_codigo import analisar_arquivo
from snapshot_comportamento import capturar, salvar

BASE = Path(__file__).resolve().parent
SNAPSHOTS = BASE / "snapshots"


def main() -> None:
    salvar(
        SNAPSHOTS / "antes_comportamento.json",
        capturar(flow.processar_fulfillment, reset=flow.reset_estado),
    )
    metricas = analisar_arquivo(BASE / "fulfillment_flow.py")
    (SNAPSHOTS / "antes_metricas.json").write_text(
        json.dumps(metricas, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Snapshots gravados em", SNAPSHOTS)


if __name__ == "__main__":
    main()
