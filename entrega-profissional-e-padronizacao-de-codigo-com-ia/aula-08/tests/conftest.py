"""Fixtures compartilhadas para testes do MVP."""

from unittest.mock import MagicMock

import pytest
from parlant.sdk import ToolContext


@pytest.fixture
def contexto_tool() -> ToolContext:
    """Contexto Parlant mínimo — tools não usam campos do context nesta fase."""
    return MagicMock(spec=ToolContext)
