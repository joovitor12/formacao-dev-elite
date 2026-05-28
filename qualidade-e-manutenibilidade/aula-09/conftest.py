"""Isola estado global do serviço entre testes."""

from __future__ import annotations

import fidelidade_service as fidelidade
import pytest


@pytest.fixture(autouse=True)
def _reset_fidelidade() -> None:
    fidelidade.reset_estado()
