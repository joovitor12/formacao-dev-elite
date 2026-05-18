"""Execute: python example.py  (ou cd pre-changes && python example.py)"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import catalogo_precos as catalogo


def main() -> None:
    print("--- Carrinho varejo ---")
    print(
        catalogo.calcular_carrinho(
            {
                "cliente_tipo": "varejo",
                "itens": [{"sku": "KIT-1", "qtd": 2, "preco_unit": 30.0}],
            }
        )
    )
    print("\n--- Carrinho atacado com volume ---")
    print(
        catalogo.calcular_carrinho(
            {
                "cliente_tipo": "atacado",
                "itens": [{"sku": "CAIXA", "qtd": 10, "preco_unit": 20.0}],
            }
        )
    )
    print("\n--- Verificacao do checklist ---")
    base = Path(__file__).resolve().parent
    subprocess.run([sys.executable, str(base / "verificar_checklist.py")], cwd=base, check=False)


if __name__ == "__main__":
    main()
