"""Execute: python example.py"""

from __future__ import annotations

import promote_build as promote


def main() -> None:
    ok = promote.promover_build("api-pedidos", "1.8.3", "staging", "prod")
    bloqueado = promote.promover_build("api-pedidos", "1.8.3", "prod", "staging")
    print("promocao ok:", ok)
    print("promocao bloqueada:", bloqueado)


if __name__ == "__main__":
    main()
