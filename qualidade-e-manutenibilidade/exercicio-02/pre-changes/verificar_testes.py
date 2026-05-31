"""Checagens automatizadas da suíte de testes do exercício integrador."""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_programa_fidelidade.py"

CHECAGENS: list[tuple[str, str, tuple[str, ...] | None, str | None]] = [
    ("regra_pura_pontos", "pontos por compra testado", ("pontos_por_compra",), None),
    ("regra_pura_premio", "custo premio testado", ("custo_premio",), None),
    ("regra_pura_borda", "borda pode_resgatar", ("pode_resgatar",), None),
    ("raises_valor_ou_tier", "erro excecao regra pura", ("pytest.raises",), None),
    ("patch_caminho_servico", "mock em fidelidade_service.*", ("fidelidade_service.", "patch"), None),
    ("sucesso_acumular", "acumular compra sucesso", ("acumular_compra", '["ok"] is true'), None),
    ("erro_retorno_saldo", "resgate saldo insuficiente", ("saldo insuficiente", '["ok"] is false'), None),
    ("erro_retorno_debitar", "falha ao debitar", ("falha ao debitar",), None),
    ("notificacao_mock", "assert em enviar_notificacao", ("enviar_notificacao", "assert_called"), None),
    ("debitar_nao_chamado", "debitar nao invocado quando saldo baixo", ("assert_not_called",), None),
    ("sem_assert_fraco", "sem anti-padroes", None, "anti_fraco"),
    ("volume_minimo", "pelo menos 10 testes", None, "contagem"),
]


def _anti_fraco(texto: str) -> bool:
    lower = texto.lower()
    if "is not none" in lower:
        return True
    if "assert true" in lower:
        return True
    if "except exception:" in lower and "pass" in lower:
        return True
    return False


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8")
    lower = texto.lower()

    print("=== Verificacao da suíte de testes ===\n")

    pendentes = 0
    for cid, descricao, marcadores, especial in CHECAGENS:
        if especial == "anti_fraco":
            pendente = _anti_fraco(texto)
        elif especial == "contagem":
            pendente = lower.count("def test_") < 10
        elif marcadores:
            pendente = not all(m in lower for m in marcadores)
        else:
            pendente = True

        status = "PENDENTE" if pendente else "OK"
        if pendente:
            pendentes += 1
        print(f"  [{status}] {cid} — {descricao}")

    print(f"\nPendentes: {pendentes}/{len(CHECAGENS)}\n")
    return 0 if pendentes == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
