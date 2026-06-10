"""Execute: python example.py"""

from __future__ import annotations

import release_gate as gate


def main() -> None:
    aprovado = gate.avaliar_release(
        {"servico": "checkout-api", "versao": "3.4.2", "score": 0.90}
    )
    reprovado = gate.avaliar_release(
        {"servico": "checkout-api", "versao": "3.4.1", "score": 0.80}
    )
    print("aprovado:", aprovado)
    print("reprovado:", reprovado)


if __name__ == "__main__":
    main()
