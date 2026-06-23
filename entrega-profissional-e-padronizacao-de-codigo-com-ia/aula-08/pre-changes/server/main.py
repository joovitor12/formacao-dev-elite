"""Bootstrap do servidor MVP — entrypoint assíncrono."""

from __future__ import annotations

import asyncio
import logging
import os

import parlant.sdk as p

from server.agent import criar_agente
from server.config import Config, obter_config
from server.guidelines import registrar_guidelines

logger = logging.getLogger(__name__)


def _configurar_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    )


def _sincronizar_env_openrouter(config: Config) -> None:
    """Garante que o adapter OpenRouter do Parlant leia a config validada."""
    os.environ["OPENROUTER_API_KEY"] = config.openrouter_api_key
    os.environ["OPENROUTER_MODEL"] = config.modelo
    os.environ["OPENROUTER_MAX_TOKENS"] = str(config.max_tokens)


async def main() -> None:
    """Sobe p.Server com OpenRouter, cria o agente e registra guidelines."""
    config = obter_config()
    _sincronizar_env_openrouter(config)

    logger.info(
        "Iniciando servidor — modelo=%s, agente=%s, max_tokens=%d",
        config.modelo,
        config.nome_agente,
        config.max_tokens,
    )

    async with p.Server(nlp_service=p.NLPServices.openrouter()) as server:
        agente = await criar_agente(server, config)
        await registrar_guidelines(agente)
        logger.info("Guidelines registradas — sandbox em http://localhost:8800")


if __name__ == "__main__":
    _configurar_logging()
    asyncio.run(main())
