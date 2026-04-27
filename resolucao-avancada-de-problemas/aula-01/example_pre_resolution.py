"""
Versão para alunos: mesmo conteúdo pedagógico que `example.py`, mas sem as correções.
Compare com `example.py` depois de resolver cada bug.

Instalação: pip install pydantic

Execute: python example_pre_resolution.py
(Comente/descomente as chamadas em main() para isolar cada falha.)
"""

from __future__ import annotations

import asyncio

from pydantic import BaseModel, ValidationError


# --- Bug 1: “mudança de schema” vs payload real (fluxo de dados) ---
# O modelo espera snake_case; o payload simula API antiga em camelCase.
class UserIn(BaseModel):
    full_name: str
    email: str


def payload_da_api() -> dict:
    return {"fullName": "Ana Dev", "email": "ana@example.com"}


def parse_usuario_bruto(data: dict) -> UserIn:
    # Intencionalmente sem alias / sem normalização — estoura ValidationError.
    return UserIn(**data)


# --- Bug 2: async + invariante do dicionário (tamanho muda durante iteração) ---
cache_metricas: dict[str, int] = {}


async def produtor_metricas() -> None:
    for i in range(50):
        cache_metricas[f"req_{i}"] = i
        await asyncio.sleep(0)


async def consumidor_metricas_errado() -> None:
    total = 0
    for chave in cache_metricas:
        await asyncio.sleep(0)
        total += cache_metricas.get(chave, 0)
        # Durante o await, o produtor aumenta o dict → RuntimeError possível.
    print("total (não deve chegar aqui se o bug disparar):", total)


async def rodar_race_dict() -> None:
    await asyncio.gather(produtor_metricas(), consumidor_metricas_errado())


# --- Bug 3: encadeamento — dado “validado” que ainda quebra mais adiante ---
class Pedido(BaseModel):
    item_id: str
    quantidade: int


def montar_linha_pedido(p: Pedido) -> str:
    # Negócio: quantidade mínima 1. Modelo permite 0 → erro lógico / divisão.
    preco_unitario = 100
    return f"subtotal={preco_unitario / p.quantidade}"


def demo_pedido_quantidade_zero() -> str:
    p = Pedido(item_id="SKU-1", quantidade=0)
    return montar_linha_pedido(p)


def main() -> None:
    print("=== Bug 1: ValidationError (camelCase vs snake_case) ===")
    try:
        u = parse_usuario_bruto(payload_da_api())
        print("usuário:", u)
    except ValidationError as e:
        print(e)

    print("\n=== Bug 2: RuntimeError (dict mudou de tamanho na iteracao) ===")
    cache_metricas.clear()
    try:
        asyncio.run(rodar_race_dict())
    except RuntimeError as e:
        print(e)

    print("\n=== Bug 3: ZeroDivisionError (Pydantic ok, regra de negocio nao) ===")
    try:
        print(demo_pedido_quantidade_zero())
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()
