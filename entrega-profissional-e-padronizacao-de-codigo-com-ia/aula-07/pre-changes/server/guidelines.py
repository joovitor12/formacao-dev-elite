"""Guidelines condicionais do assistente."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


async def registrar_guidelines(agente: Any) -> None:
    """Registra guidelines de escopo, tom e segurança no agente."""
    # TODO: implementar ≥ 3 guidelines (escopo_mvp.md):
    #   - escopo da Formação Dev Elite
    #   - honestidade (não inventar URLs ou módulos)
    #   - tom em português claro
    #   - segurança (não expor API keys)
    logger.debug(
        "registrar_guidelines ainda não implementado (agente=%s)",
        getattr(agente, "name", "desconhecido"),
    )
