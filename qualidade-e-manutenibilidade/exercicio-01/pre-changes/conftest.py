"""Isola estado global entre testes."""

from __future__ import annotations

import fulfillment_baseline as baseline
import fulfillment_flow as flow
import pytest


@pytest.fixture(autouse=True)
def _reset_modulos() -> None:
    flow.reset_estado()
    baseline.reset_estado()
