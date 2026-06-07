"""Execute: python example.py"""

from __future__ import annotations

import rollback_service as rollback


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


if __name__ == "__main__":
    main()
