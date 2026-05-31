"""Checklist de anti-padroes + delegacao ao simulador de regressao."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_politica_reembolso.py"
SIMULADOR = BASE / "simular_regressao.py"

ANTI_PADROES: list[tuple[str, str, tuple[str, ...]]] = [
    ("assert_somente_ok", "assert so ok is True", ('["ok"] is true',)),
    ("except_pass", "except generico com pass", ("except exception:", "pass")),
    ("assert_true_except", "assert true no except", ("assert true",)),
    (
        "percentual_sem_valor",
        "percentual sem valor_reembolso no mesmo teste",
        ("percentual",),
    ),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8").lower()

    print("=== Anti-padroes em test_politica_reembolso.py ===\n")
    padroes = 0
    for aid, descricao, marcadores in ANTI_PADROES:
        if aid == "percentual_sem_valor":
            presente = "percentual" in texto and "valor_reembolso" not in texto.split("test_meio_prazo")[1].split("def ")[0] if "test_meio_prazo" in texto else False
        elif aid == "assert_somente_ok":
            bloco = texto.split("test_reembolso_padrao_aprovado")[1].split("def ")[0] if "test_reembolso_padrao_aprovado" in texto else ""
            presente = '["ok"] is true' in bloco and "valor_reembolso" not in bloco
        else:
            presente = all(m in texto for m in marcadores)

        status = "PENDENTE" if presente else "OK"
        if presente:
            padroes += 1
        print(f"  [{status}] {aid} — {descricao}")

    print(f"\nAnti-padroes pendentes: {padroes}/{len(ANTI_PADROES)}\n")

    print("=== Simulador de regressao ===\n")
    proc = subprocess.run([sys.executable, str(SIMULADOR)], cwd=BASE, check=False)
    sim_ok = proc.returncode == 0

    if padroes == 0 and sim_ok:
        print("\nVerificacao completa: nenhuma lacuna conhecida.\n")
        return 0

    print("\nAjuste testes com guia_falsos_positivos.md antes de entregar.\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
