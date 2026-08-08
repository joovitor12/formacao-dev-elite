"""Execute: python example.py"""

from __future__ import annotations

import promote_build as promote


def main() -> None:
    sem_confirmar = promote.promover_build(
        "api-pedidos", "1.8.3", "staging", "prod"
    )
    com_confirmar = promote.promover_build(
        "api-pedidos", "1.8.3", "staging", "prod", confirmar_prod=True
    )
    bloqueado = promote.promover_build("api-pedidos", "1.8.3", "prod", "staging")
    print("sem confirmar:", sem_confirmar)
    print("com confirmar:", com_confirmar)
    print("bloqueado:", bloqueado)


if __name__ == "__main__":
    main()
