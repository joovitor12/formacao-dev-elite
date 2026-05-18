"""Métricas estruturais simples para comparar código antes vs depois."""

from __future__ import annotations

import re
from pathlib import Path


def analisar_arquivo(caminho: Path) -> dict[str, int]:
    texto = caminho.read_text(encoding="utf-8")
    linhas = [
        linha
        for linha in texto.splitlines()
        if linha.strip() and not linha.strip().startswith("#")
    ]
    funcoes = len(re.findall(r"^def ", texto, flags=re.MULTILINE))
    ramos = (
        texto.count("if ")
        + texto.count("elif ")
        + texto.count("for ")
        + texto.count("while ")
    )
    return {
        "loc": len(linhas),
        "funcoes": funcoes,
        "ramos_aprox": ramos,
    }
