"""Execute: python example.py"""

from __future__ import annotations

import pipeline_review as pipeline


def main() -> None:
    print(pipeline.notificar_deploy({"ambiente": "staging", "versao": "1.2.0"}))
    print("rollback 0.05:", pipeline.deve_rollback(0.05, 200))
    print("merge prod:", pipeline.pode_mergear_pipeline("prod", 1, True))


if __name__ == "__main__":
    main()
