"""Casos usados para provar equivalência funcional entre service e baseline."""

from __future__ import annotations

from typing import Any

CASOS: list[dict[str, Any]] = [
    {
        "id": "junior_produto_basico",
        "entrada": {
            "vendedor_nivel": "junior",
            "valor_venda": 1000.0,
            "categoria": "produto",
            "meta_bateu": False,
        },
    },
    {
        "id": "junior_servico_leve",
        "entrada": {
            "vendedor_nivel": "junior",
            "valor_venda": 200.0,
            "categoria": "servico",
            "meta_bateu": False,
        },
    },
    {
        "id": "pleno_produto_com_meta",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 500.0,
            "categoria": "produto",
            "meta_bateu": True,
        },
    },
    {
        "id": "senior_servico_alto_valor_meta",
        "entrada": {
            "vendedor_nivel": "senior",
            "valor_venda": 15000.0,
            "categoria": "servico",
            "meta_bateu": True,
        },
    },
    {
        "id": "senior_produto_acima_dez_mil",
        "entrada": {
            "vendedor_nivel": "senior",
            "valor_venda": 12000.0,
            "categoria": "produto",
            "meta_bateu": False,
        },
    },
    {
        "id": "valor_zero",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 0.0,
            "categoria": "produto",
        },
    },
    {
        "id": "nivel_invalido",
        "entrada": {
            "vendedor_nivel": "estagiario",
            "valor_venda": 100.0,
            "categoria": "produto",
        },
    },
    {
        "id": "categoria_invalida",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 100.0,
            "categoria": "assinatura",
        },
    },
    {
        "id": "pleno_servico_sem_meta",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 2500.0,
            "categoria": "servico",
            "meta_bateu": False,
        },
    },
    {
        "id": "senior_produto_limite_dez_mil",
        "entrada": {
            "vendedor_nivel": "senior",
            "valor_venda": 10000.0,
            "categoria": "produto",
            "meta_bateu": True,
        },
    },
    {
        "id": "pleno_produto_meta_ausente_valido",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 500.0,
            "categoria": "produto",
        },
    },
    {
        "id": "senior_servico_limite_exato_dez_mil_sem_meta",
        "entrada": {
            "vendedor_nivel": "senior",
            "valor_venda": 10000.0,
            "categoria": "servico",
            "meta_bateu": False,
        },
    },
    {
        "id": "senior_servico_um_centavo_acima_dez_mil",
        "entrada": {
            "vendedor_nivel": "senior",
            "valor_venda": 10000.01,
            "categoria": "servico",
            "meta_bateu": False,
        },
    },
    {
        "id": "normalizacao_maiusculas_pleno_servico_com_meta",
        "entrada": {
            "vendedor_nivel": "PLENO",
            "valor_venda": 1000.0,
            "categoria": "SERVICO",
            "meta_bateu": True,
        },
    },
    {
        "id": "multiplos_erros_prioriza_valor_invalido",
        "entrada": {
            "vendedor_nivel": "estagiario",
            "valor_venda": -10.0,
            "categoria": "assinatura",
            "meta_bateu": True,
        },
    },
    {
        "id": "meta_string_false_conta_como_true_por_coercao",
        "entrada": {
            "vendedor_nivel": "pleno",
            "valor_venda": 500.0,
            "categoria": "produto",
            "meta_bateu": "false",
        },
    }
]
