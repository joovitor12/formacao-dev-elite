"""Execute: python example.py"""

from __future__ import annotations

import logging
import os

import rollback_service as rollback

logging.basicConfig(level=logging.INFO)


def main() -> None:
    print("--- should_rollback (fronteira 0.05) ---")
    print("0.05 / 200 ->", rollback.should_rollback(0.05, 200))
    print("0.06 / 200 ->", rollback.should_rollback(0.06, 200))

    print("\n--- executar_rollback prod sem confirmacao ---")
    print(
        rollback.executar_rollback(
            "prod", "2.0.1", "2.0.0", confirmado=False
        )
    )

    print("\n--- executar_rollback dev (sem chave de API) ---")
    os.environ.pop("ROLLBACK_API_KEY", None)
    print(rollback.executar_rollback("dev", "2.0.1", "2.0.0"))

    print("\n--- executar_rollback prod confirmado ---")
    os.environ["ROLLBACK_API_KEY"] = "rk_example_placeholder"
    print(
        rollback.executar_rollback(
            "prod", "2.0.1", "2.0.0", confirmado=True
        )
    )


if __name__ == "__main__":
    main()
