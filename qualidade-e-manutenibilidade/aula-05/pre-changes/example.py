"""Execute: cd pre-changes && python example.py"""

from __future__ import annotations

import estoque_service as estoque


def main() -> None:
    print("Saldo inicial SKU-A:", estoque.consultar_saldo("SKU-A"))
    print("Entrada:", estoque.registrar_movimento({"tipo": "entrada", "sku": "SKU-A", "qtd": 5}))
    print("Saída:", estoque.registrar_movimento({"tipo": "saida", "sku": "SKU-A", "qtd": 2}))
    print("Tentativa inválida:", estoque.registrar_movimento({"tipo": "saida", "sku": "SKU-A", "qtd": 999}))
    print("Auditoria (último):", estoque.listar_auditoria()[-1:])


if __name__ == "__main__":
    main()
