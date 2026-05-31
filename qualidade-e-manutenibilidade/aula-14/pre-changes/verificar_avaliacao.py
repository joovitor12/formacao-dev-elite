"""Detecta anti-padrões ainda presentes em test_campanha_desconto.py."""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_campanha_desconto.py"

# (id, descricao curta, marcadores que indicam problema AINDA presente)
ANTI_PADROES: list[tuple[str, str, tuple[str, ...]]] = [
    (
        "assert_is_not_none",
        "assert fraco (is not None)",
        ("is not none",),
    ),
    (
        "try_except_assert_true",
        "excecao com assert True",
        ("assert true",),
    ),
    (
        "excecao_engolida",
        "except generico com pass",
        ("except exception:", "pass"),
    ),
    (
        "teste_monolitico",
        "varios comportamentos no mesmo teste",
        ("test_cupom_e_desconto_no_mesmo_teste",),
    ),
    (
        "erro_sem_pytest_raises",
        "cenario de erro sem pytest.raises",
        ("pytest.raises",),
    ),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8")
    texto_lower = texto.lower()

    print("=== Anti-padroes vs testes atuais ===\n")

    pendentes = 0
    for aid, descricao, marcadores in ANTI_PADROES:
        if aid == "erro_sem_pytest_raises":
            # Pendente enquanto NAO houver pytest.raises no arquivo
            presente = "pytest.raises" not in texto_lower
        else:
            presente = all(m in texto_lower for m in marcadores)

        status = "PENDENTE" if presente else "OK"
        if presente:
            pendentes += 1
        print(f"  [{status}] {aid} — {descricao}")

    print(f"\nPendentes: {pendentes}/{len(ANTI_PADROES)}")
    print("(Baseline inicial costuma ter varios PENDENTE — corrija apos avaliar.)\n")
    return 0 if pendentes == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
