"""Checklist: cenários da matriz vs menções em test_regras_resgate.py."""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_regras_resgate.py"

# (id, palavras que indicam cobertura no arquivo de teste)
CENARIOS: list[tuple[str, tuple[str, ...]]] = [
    ("sucesso_saldo_maior", ("saldo_suficiente", "120")),
    ("sucesso_saldo_exato", ("saldo_exato",)),
    ("erro_codigo_vazio", ("codigo_obrigatorio", "codigo vazio")),
    ("erro_codigo_invalido", ("codigo invalido", "codigo_invalido")),
    ("erro_saldo_negativo", ("saldo invalido", "saldo_negativo")),
    ("erro_saldo_insuficiente", ("saldo insuficiente", "saldo_insuficiente")),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8").lower()
    print("=== Cenarios vs testes atuais ===\n")

    pendentes = 0
    for cid, marcadores in CENARIOS:
        coberto = any(m in texto for m in marcadores)
        status = "OK" if coberto else "PENDENTE"
        if not coberto:
            pendentes += 1
        print(f"  [{status}] {cid}")

    print(f"\nPendentes: {pendentes}/{len(CENARIOS)}")
    print("(Erros costumam ficar PENDENTE no baseline inicial.)\n")
    return 0 if pendentes == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
