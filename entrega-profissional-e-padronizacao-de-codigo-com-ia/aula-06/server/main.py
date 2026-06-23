"""Bootstrap do servidor MVP — entrypoint assíncrono."""

from __future__ import annotations

import asyncio
import logging

from server.config import obter_config

logger = logging.getLogger(__name__)


def _configurar_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    )


async def main() -> None:
    """Valida configuração local. p.Server na entrega seguinte (ADR-007)."""
    config = obter_config()
    logger.info(
        "Config validada — modelo=%s, agente=%s, max_tokens=%d",
        config.modelo,
        config.nome_agente,
        config.max_tokens,
    )
    # TODO: async with p.Server(...) as server:
    #           agente = await criar_agente(server, config)
    #           await registrar_guidelines(agente)


if __name__ == "__main__":
    _configurar_logging()
    asyncio.run(main())
