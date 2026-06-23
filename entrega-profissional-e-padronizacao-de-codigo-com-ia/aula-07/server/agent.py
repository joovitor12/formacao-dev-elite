"""Criação do agente Parlant."""

from __future__ import annotations

import logging
from typing import Any

from server.config import Config

logger = logging.getLogger(__name__)


async def criar_agente(server: Any, config: Config) -> Any:
    """Instancia o agente de onboarding no servidor Parlant."""
    agente = await server.create_agent(
        name=config.nome_agente,
        description=config.descricao_agente,
    )
    logger.info("Agente criado: %s", config.nome_agente)
    return agente
