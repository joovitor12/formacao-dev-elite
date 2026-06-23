"""Guidelines condicionais do assistente."""

from __future__ import annotations

import logging

from parlant.sdk import Agent

from server.tools.visao_geral import consultar_visao_geral_projeto

logger = logging.getLogger(__name__)


async def registrar_guidelines(agente: Agent) -> None:
    """Registra guidelines de escopo, tom e segurança no agente."""
    await agente.create_guideline(
        condition="o usuário faz uma pergunta ou comentário",
        action=(
            "Responda apenas sobre a Formação Dev Elite, onboarding do curso "
            "e materiais deste repositório. Recuse educadamente assuntos "
            "sem relação com a formação."
        ),
    )

    await agente.create_guideline(
        condition="você não tem certeza da resposta ou falta informação confiável",
        action=(
            "Diga claramente que não sabe. Não invente URLs, nomes de módulos, "
            "links ou detalhes técnicos."
        ),
    )

    await agente.create_guideline(
        condition="o usuário faz uma pergunta ou pede orientação",
        action=(
            "Use português claro e objetivo. Prefira respostas curtas, "
            "a menos que o usuário peça mais detalhes."
        ),
    )

    await agente.create_guideline(
        condition=(
            "o usuário pede, menciona ou tenta compartilhar API keys, tokens, "
            "senhas ou dados pessoais"
        ),
        action=(
            "Recuse fornecer ou repetir credenciais e dados sensíveis. "
            "Oriente o usuário a configurar variáveis de ambiente locais (.env) "
            "sem expor segredos no chat."
        ),
    )

    await agente.create_guideline(
        condition=(
            "o usuário pergunta sobre a stack, tecnologias, arquitetura ou "
            "componentes do MVP chatbot deste projeto"
        ),
        action=(
            "Chame a tool consultar_visao_geral_projeto e responda com base "
            "no conteúdo retornado. Não invente tecnologias além do documento."
        ),
        tools=[consultar_visao_geral_projeto],
    )

    logger.info("Guidelines registradas para o agente %s", agente.name)
