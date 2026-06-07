"""Execute: python example.py"""

from __future__ import annotations

import deploy_notifier as notifier


def main() -> None:
    out = notifier.processar_deploy(
        {"ambiente": "prod", "versao": "2.1.0", "status": "sucesso"}
    )
    print(out)
    print("ultimo prod:", notifier.consultar_ultimo_deploy("prod"))


if __name__ == "__main__":
    main()
