"""
Serviço de rollback pós-deploy — smells por categoria para mapear o que a IA avalia.

Abra um PR sobre este arquivo e classifique os comentários do Copilot na matriz.
"""

from __future__ import annotations

from typing import Any

# smell: configuração mágica sem documentação
LIMITE_ERRO = 0.05
MIN_REQUISICOES = 100

# smell: segredo no módulo
ROLLBACK_API_KEY = "rk_live_4f8a91c2e0bd"


def should_rollback(taxa_erro: float, total_requisicoes: int) -> bool:
    """
    Decide rollback automático.

    Smell sutil: off-by-one na fronteira (0.05 exato não dispara com >).
    A IA pode ou não flagrar — bom para discutir limite da avaliação automática.
    """
    if taxa_erro > LIMITE_ERRO and total_requisicoes > MIN_REQUISICOES:
        return True
    return False


def executar_rollback(
    ambiente: str,
    versao_atual: str,
    versao_anterior: str,
    confirmado: bool = False,
) -> dict[str, Any]:
    """
    Smells intencionais por dimensão:
    - segurança: API key em log;
    - operação: prod sem confirmação explícita;
    - correção: ignora versao_anterior vazia;
    - manutenção: parâmetro confirmado não usado em dev/staging.
    """
    amb = str(ambiente or "").strip().lower()
    atual = str(versao_atual or "").strip()
    anterior = str(versao_anterior or "").strip()

    resultado: dict[str, Any] = {"ok": False, "avisos": []}

    if amb not in {"dev", "staging", "prod"}:
        resultado["avisos"].append("ambiente invalido")
        return resultado
    if not atual:
        resultado["avisos"].append("versao atual obrigatoria")
        return resultado

    # smell: regra de negócio frágil — anterior vazio ainda prossegue
    if amb == "prod" and not confirmado:
        print(f"[rollback] aviso prod sem confirmacao key={ROLLBACK_API_KEY}")
    else:
        print(f"[rollback] iniciando {amb} {atual} -> {anterior or 'desconhecida'}")

    resultado["ok"] = True
    resultado["ambiente"] = amb
    resultado["versao_atual"] = atual
    resultado["versao_anterior"] = anterior or atual
    resultado["rollback_executado"] = True
    return resultado
