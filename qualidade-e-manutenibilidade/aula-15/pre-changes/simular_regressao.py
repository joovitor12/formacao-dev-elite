"""
Simula regressões e verifica se a suíte atual ainda passaria (falso positivo).

Cada probe injeta dado bugado ou inspeciona o teste — se a lacuna permanece,
o cenário ainda é falso positivo de confiança.
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTE = BASE / "test_politica_reembolso.py"


def _bloco_teste(nome: str, texto: str) -> str:
    if f"def {nome}" not in texto:
        return ""
    return texto.split(f"def {nome}")[1].split("\ndef ")[0].lower()


def _probe_apenas_ok(texto: str) -> bool:
    bloco = _bloco_teste("test_reembolso_padrao_aprovado", texto)
    if not bloco:
        return True
    if "valor_reembolso" in bloco or "percentual" in bloco:
        return False
    bugado = {"ok": True, "valor_reembolso": 0.01}
    try:
        assert bugado["ok"] is True
        return True
    except AssertionError:
        return False


def _probe_prazo_expirado(texto: str) -> bool:
    bloco = _bloco_teste("test_prazo_expirado_rejeita", texto)
    if not bloco:
        return True
    if '["ok"] is false' in bloco and "prazo expirado" in bloco:
        return False
    if "except exception" in bloco and "pass" in bloco:
        return True
    return "prazo expirado" not in bloco


def _probe_percentual_sem_valor(texto: str) -> bool:
    bloco = _bloco_teste("test_meio_prazo_aplica_cinquenta_porcento", texto)
    if not bloco:
        return True
    if "valor_reembolso" in bloco:
        return False
    bugado = {"percentual": 0.5, "valor_reembolso": 999.0}
    try:
        assert bugado["percentual"] == 0.5
        return True
    except AssertionError:
        return False


def _probe_valor_invalido(texto: str) -> bool:
    bloco = _bloco_teste("test_valor_invalido_dispara_erro", texto)
    if not bloco:
        return True
    if "pytest.raises" in bloco:
        return False
    return "assert true" in bloco or ("except valueerror" in bloco and "match" not in bloco)


PROBES: list[tuple[str, str, str]] = [
    ("apenas_ok_true", "test_reembolso_padrao_aprovado", "só ok ou assert incompleto"),
    ("prazo_expirado_engolido", "test_prazo_expirado_rejeita", "except/pass ou falta assert de falha"),
    ("percentual_sem_valor", "test_meio_prazo_aplica_cinquenta_porcento", "percentual sem valor_reembolso"),
    ("erro_fraco", "test_valor_invalido_dispara_erro", "sem pytest.raises idiomático"),
]


def main() -> int:
    texto = TESTE.read_text(encoding="utf-8").lower()

    print("=== Simulacao de regressao (falsos positivos) ===\n")

    funcoes = [
        _probe_apenas_ok,
        _probe_prazo_expirado,
        _probe_percentual_sem_valor,
        _probe_valor_invalido,
    ]

    lacunas = 0
    for (pid, teste, descricao), probe in zip(PROBES, funcoes, strict=True):
        ainda_passa = probe(texto)
        status = "LACUNA" if ainda_passa else "DETECTA"
        if ainda_passa:
            lacunas += 1
        print(f"  [{status}] {pid} ({teste})")
        print(f"           {descricao}\n")

    print(f"Lacunas: {lacunas}/{len(PROBES)}")
    print("(LACUNA = teste ainda passaria com bug simulado — ajuste os asserts.)\n")
    return 0 if lacunas == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
