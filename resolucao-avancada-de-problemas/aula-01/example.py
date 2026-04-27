"""
Exemplos propositalmente ERRADOS — Aula 36 (debugging com agente).

Instalação: pip install pydantic

Execute: python aula-01.py
(Comente/descomente as chamadas em main() para isolar cada falha.)
"""

from __future__ import annotations

import asyncio

from pydantic import BaseModel, ConfigDict, Field, ValidationError


# --- Bug 1 (corrigido): payload em camelCase vs campos snake_case no modelo ---
# `fullName` na API mapeia para `full_name` via alias; populate_by_name permite
# construir/validar por nome Python ou pelo alias.
class UserIn(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    full_name: str = Field(alias="fullName")
    email: str


def payload_da_api() -> dict:
    return {"fullName": "Ana Dev", "email": "ana@example.com"}


def parse_usuario_bruto(data: dict) -> UserIn:
    return UserIn(**data)


# --- Bug 2 (corrigido): snapshot das chaves antes de iterar ---
# Iterar diretamente sobre o dict enquanto outra tarefa insere chaves durante
# `await` estoura RuntimeError; `list(keys)` fixa o conjunto de chaves neste ponto.
cache_metricas: dict[str, int] = {}


async def produtor_metricas() -> None:
    for i in range(50):
        cache_metricas[f"req_{i}"] = i
        await asyncio.sleep(0)


async def consumidor_metricas() -> None:
    await asyncio.sleep(0)
    total = 0
    # Snapshot após ceder o loop: evita iterar sobre {} se o consumidor rodar primeiro.
    for chave in list(cache_metricas.keys()):
        await asyncio.sleep(0)
        total += cache_metricas.get(chave, 0)
    print("total (sobre snapshot inicial de chaves):", total)


async def rodar_race_dict() -> None:
    await asyncio.gather(produtor_metricas(), consumidor_metricas())


# --- Bug 3 (corrigido): quantidade mínima 1 no modelo — evita divisão por zero ---
class Pedido(BaseModel):
    item_id: str
    quantidade: int = Field(ge=1)


def montar_linha_pedido(p: Pedido) -> str:
    preco_unitario = 100
    return f"subtotal={preco_unitario / p.quantidade}"


def demo_pedido_quantidade_zero() -> str:
    p = Pedido(item_id="SKU-1", quantidade=1)
    return montar_linha_pedido(p)


def main() -> None:
    print("=== Bug 1: UserIn com alias fullName -> full_name ===")
    try:
        u = parse_usuario_bruto(payload_da_api())
        print("usuário:", u)
    except ValidationError as e:
        print(e)

    print("\n=== Bug 2: consumidor com snapshot list(cache_metricas.keys()) ===")
    cache_metricas.clear()
    asyncio.run(rodar_race_dict())

    print("\n=== Bug 3: quantidade 0 barrada por Field(ge=1) ===")
    try:
        print(demo_pedido_quantidade_zero())
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
