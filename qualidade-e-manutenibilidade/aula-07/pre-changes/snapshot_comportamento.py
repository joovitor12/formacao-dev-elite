"""Captura saídas de calcular_cobranca para comparar antes vs depois."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from casos_cobranca import CASOS


def capturar(
    calcular: Callable[[dict[str, Any]], dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {"id": caso["id"], "saida": calcular(caso["entrada"])} for caso in CASOS
    ]


def salvar(caminho: Path, registros: list[dict[str, Any]]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(
        json.dumps(registros, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def carregar(caminho: Path) -> list[dict[str, Any]]:
    return json.loads(caminho.read_text(encoding="utf-8"))
