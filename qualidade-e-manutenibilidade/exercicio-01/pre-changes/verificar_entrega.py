"""Portão final do exercício integrador."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def _run(cmd: list[str]) -> int:
    proc = subprocess.run(cmd, cwd=BASE)
    return proc.returncode


def main() -> int:
    print("=== Verificacao de entrega — Operacao Fulfillment ===\n")

    etapas = [
        ("pytest -q", [sys.executable, "-m", "pytest", "-q"]),
        (
            "equivalencia funcional",
            [sys.executable, "-m", "pytest", "-q", "test_equivalencia_funcional.py"],
        ),
        ("relatorio antes vs depois", [sys.executable, "relatorio_antes_depois.py"]),
        ("checklist", [sys.executable, "verificar_checklist.py"]),
    ]

    falhas = 0
    for nome, cmd in etapas:
        codigo = _run(cmd)
        status = "OK" if codigo == 0 else "FALHOU"
        print(f"[{status}] {nome}")
        if codigo != 0:
            falhas += 1

    ignorar = {
        "fulfillment_flow.py",
        "fulfillment_baseline.py",
        "casos_equivalencia.py",
        "conftest.py",
        "metricas_codigo.py",
        "snapshot_comportamento.py",
        "relatorio_antes_depois.py",
        "gerar_snapshots_antes.py",
        "verificar_checklist.py",
        "verificar_entrega.py",
        "example.py",
    }
    modulos_extra = [
        p.name
        for p in BASE.glob("*.py")
        if p.name not in ignorar and not p.name.startswith("test_")
    ]
    if len(modulos_extra) >= 2:
        print(f"[OK] modulos extra detectados: {', '.join(sorted(modulos_extra))}")
    else:
        print(
            "[AVISO] criterio pede >= 2 modulos de responsabilidade "
            f"(encontrados: {len(modulos_extra)})"
        )
        falhas += 1

    if falhas:
        print(f"\nEntrega incompleta ({falhas} pendencia(s)).")
        return 1

    print("\nEntrega OK — todos os portoes passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
