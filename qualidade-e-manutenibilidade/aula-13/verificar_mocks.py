"""Checklist: cenários de mock vs menções em test_resgate_service.py."""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_resgate_service.py"


def _coberto(texto: str, marcadores: tuple[str, ...]) -> bool:
    return all(m in texto for m in marcadores)


def _coberto_um_de(texto: str, opcoes: tuple[tuple[str, ...], ...]) -> bool:
    return any(_coberto(texto, grupo) for grupo in opcoes)


CENARIOS: list[tuple[str, tuple[str, ...] | None, tuple[tuple[str, ...], ...] | None]] = [
    ("regra_pura_local", ("custo_resgate",), None),
    (
        "patch_caminho_servico",
        ("resgate_service.", "patch"),
        None,
    ),
    (
        "cenario_saldo_insuficiente",
        ("saldo insuficiente", "executar_resgate"),
        None,
    ),
    ("cenario_falha_debito", ("falha ao debitar", "executar_resgate"), None),
    (
        "verifica_notificacao",
        ("enviar_confirmacao",),
        (
            ("assert_called",),
            ("called_once",),
            ("call_args",),
        ),
    ),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8").lower()
    print("=== Cenarios de mock vs testes atuais ===\n")

    pendentes = 0
    for item in CENARIOS:
        cid = item[0]
        obrigatorios = item[1]
        alternativas = item[2]

        if obrigatorios and alternativas:
            coberto = _coberto(texto, obrigatorios) and _coberto_um_de(texto, alternativas)
        elif obrigatorios:
            coberto = _coberto(texto, obrigatorios)
        else:
            coberto = False

        status = "OK" if coberto else "PENDENTE"
        if not coberto:
            pendentes += 1
        print(f"  [{status}] {cid}")

    print(f"\nPendentes: {pendentes}/{len(CENARIOS)}")
    print("(Orquestracao com mock costuma ficar PENDENTE no baseline inicial.)\n")
    return 0 if pendentes == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
