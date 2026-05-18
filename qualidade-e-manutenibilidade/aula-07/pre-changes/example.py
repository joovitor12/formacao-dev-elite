"""Execute: python example.py  (ou cd pre-changes && python relatorio_antes_depois.py)"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    script = base / "relatorio_antes_depois.py"
    print("Rodando relatório antes vs depois...\n")
    subprocess.run([sys.executable, str(script)], cwd=base, check=False)


if __name__ == "__main__":
    main()
