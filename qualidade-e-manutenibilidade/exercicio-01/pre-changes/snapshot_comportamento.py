"""Captura saídas de processar_fulfillment para comparar antes vs depois."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from casos_equivalencia import CASOS


def capturar(
    processar: Callable[[dict[str, Any]], dict[str, Any]],
    reset: Callable[[], None] | None = None,
) -> list[dict[str, Any]]:
    registros: list[dict[str, Any]] = []
    for caso in CASOS:
        if reset:
            reset()
        registros.append({"id": caso["id"], "saida": processar(caso["entrada"])})
    return registros


def salvar(caminho: Path, registros: list[dict[str, Any]]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(
        json.dumps(registros, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def carregar(caminho: Path) -> list[dict[str, Any]]:
    return json.loads(caminho.read_text(encoding="utf-8"))
