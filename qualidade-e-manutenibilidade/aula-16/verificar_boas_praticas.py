"""Checklist automatizado de boas práticas em test_ativacao_service.py."""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_ativacao_service.py"

# (id, descricao, marcadores obrigatorios OU logica especial)
CHECAGENS: list[tuple[str, str, tuple[str, ...] | None, str | None]] = [
    ("regra_pura_local", "teste de regra pura sem mock", ("creditos_por_tier", "ouro"), None),
    ("patch_caminho_servico", "mock no modulo ativacao_service", ("ativacao_service.", "patch"), None),
    ("sucesso_orquestracao", "cenario de sucesso ativar_tier", ("ativar_tier", '["ok"] is true'), None),
    ("erro_excecao_raises", "tier invalido com pytest.raises", ("pytest.raises", "tier invalido"), None),
    ("erro_retorno_saldo", "saldo insuficiente ok false", ("saldo insuficiente", '["ok"] is false'), None),
    ("assert_recibo_mock", "verifica envio de recibo no mock", ("enviar_recibo", "assert_called"), None),
    ("sem_assert_fraco", "sem anti-padroes de assert", None, "anti_fraco"),
    ("nomes_descritivos", "sem test_1 / test_2 genericos", None, "nomes"),
    ("volume_minimo", "pelo menos 5 testes nomeados", None, "contagem"),
]


def _anti_fraco(texto: str) -> bool:
    """True se ainda ha anti-padrao (pendente)."""
    lower = texto.lower()
    if "is not none" in lower:
        return True
    if "assert true" in lower:
        return True
    if "except exception:" in lower and "pass" in lower:
        return True
    return False


def _nomes_genericos(texto: str) -> bool:
    lower = texto.lower()
    return "def test_1" in lower or "def test_2" in lower or "def test_ok" in lower


def _contagem_insuficiente(texto: str) -> bool:
    return texto.lower().count("def test_") < 5


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8")
    lower = texto.lower()

    print("=== Boas praticas vs test_ativacao_service.py ===\n")

    pendentes = 0
    for cid, descricao, marcadores, especial in CHECAGENS:
        if especial == "anti_fraco":
            pendente = _anti_fraco(texto)
        elif especial == "nomes":
            pendente = _nomes_genericos(texto)
        elif especial == "contagem":
            pendente = _contagem_insuficiente(texto)
        elif marcadores:
            pendente = not all(m in lower for m in marcadores)
        else:
            pendente = True

        status = "PENDENTE" if pendente else "OK"
        if pendente:
            pendentes += 1
        print(f"  [{status}] {cid} — {descricao}")

    print(f"\nPendentes: {pendentes}/{len(CHECAGENS)}")
    print("(Baseline inicial costuma ter varias pendencias — complete com IA + guia.)\n")
    return 0 if pendentes == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
