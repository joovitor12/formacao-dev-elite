"""Probes de falso positivo — lacunas ainda presentes na suíte."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_programa_fidelidade.py"


def _bloco(nome: str, texto: str) -> str:
    if f"def {nome}" not in texto:
        return ""
    return texto.split(f"def {nome}")[1].split("\ndef ")[0].lower()


def _probe_is_not_none(texto: str) -> bool:
    return "is not none" in texto.lower()


def _probe_assert_true(texto: str) -> bool:
    return "assert true" in texto.lower()


def _probe_except_pass(texto: str) -> bool:
    lower = texto.lower()
    return "except exception:" in lower and "pass" in lower


def _probe_pode_resgatar_sem_prova(texto: str) -> bool:
    lower = texto.lower()
    if "pode_resgatar" not in lower:
        return True
    if "is false" in lower or "is true" in lower:
        return False
    bloco = _bloco("test_resgate_saldo_baixo", texto)
    return bool(bloco) and "assert" not in bloco


PROBES: list[tuple[str, Callable[[str], bool]]] = [
    ("assert_is_not_none", _probe_is_not_none),
    ("try_except_assert_true", _probe_assert_true),
    ("except_pass", _probe_except_pass),
    ("pode_resgatar_sem_prova", _probe_pode_resgatar_sem_prova),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8")

    print("=== Simulacao de falsos positivos ===\n")

    lacunas = 0
    for pid, probe in PROBES:
        ativo = probe(texto)
        status = "LACUNA" if ativo else "OK"
        if ativo:
            lacunas += 1
        print(f"  [{status}] {pid}")

    print(f"\nLacunas: {lacunas}/{len(PROBES)}\n")
    return 0 if lacunas == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
