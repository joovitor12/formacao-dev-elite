"""Execute: python example.py  (ou cd pre-changes && python example.py)"""

from __future__ import annotations

import regras_assinatura as assinatura


def main() -> None:
    print("Mensal basico:", assinatura.valor_plano("basico"))
    print("Fatura pro 12m + ativacao:", assinatura.calcular_fatura("pro", 12, primeira_fatura=True))


if __name__ == "__main__":
    main()
