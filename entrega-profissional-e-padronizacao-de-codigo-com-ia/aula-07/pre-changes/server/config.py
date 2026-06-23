"""Configuração e constantes do servidor — carrega segredos via .env."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

NOME_AGENTE = "assistente-formacao"
DESCRICAO_AGENTE = "Assistente de onboarding da Formação Dev Elite."
MODELO_PADRAO = "openrouter/owl-alpha"
MAX_TOKENS_PADRAO = 128_000

_BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Config:
    """Configuração validada do servidor MVP."""

    openrouter_api_key: str
    modelo: str
    nome_agente: str
    descricao_agente: str
    max_tokens: int


def _carregar_env() -> None:
    load_dotenv(_BASE_DIR / ".env")


def _obter_modelo() -> str:
    return os.getenv("OPENROUTER_MODEL") or os.getenv("PARLANT_MODEL") or MODELO_PADRAO


def _obter_max_tokens() -> int:
    valor = os.getenv("OPENROUTER_MAX_TOKENS", str(MAX_TOKENS_PADRAO))
    try:
        return int(valor)
    except ValueError as exc:
        msg = "OPENROUTER_MAX_TOKENS deve ser um inteiro."
        raise ValueError(msg) from exc


def obter_config() -> Config:
    """Carrega e valida variáveis de ambiente. Nunca expõe a API key em logs."""
    _carregar_env()

    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not api_key or api_key.startswith("sk-or-v1-substitua"):
        msg = (
            "OPENROUTER_API_KEY ausente ou placeholder. "
            "Copie .env.example para .env e preencha sua chave."
        )
        raise ValueError(msg)

    return Config(
        openrouter_api_key=api_key,
        modelo=_obter_modelo(),
        nome_agente=NOME_AGENTE,
        descricao_agente=DESCRICAO_AGENTE,
        max_tokens=_obter_max_tokens(),
    )
