"""Execute: python example.py"""

from __future__ import annotations

import release_gate as gate


def main() -> None:
    out = gate.avaliar_release(
        {"servico": "checkout-api", "versao": "3.4.2", "score": 0.90}
    )
    print(out)
    print("validacoes:", gate.consultar_validacoes())


if __name__ == "__main__":
    main()
