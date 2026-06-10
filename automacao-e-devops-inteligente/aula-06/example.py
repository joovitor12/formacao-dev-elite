"""Execute: python example.py"""

from __future__ import annotations

import merge_policy as policy


def main() -> None:
    print(
        "prod 0 humano + copilot:",
        policy.pode_mergear("prod", 0, False, copilot_aprovou=True),
    )
    print(
        "prod forcar_merge:",
        policy.pode_mergear("prod", 0, False, forcar_merge=True),
    )
    print(
        "prod bot como aprovador:",
        policy.pode_mergear(
            "prod", 0, False, aprovadores=["copilot-bot", "github-actions"]
        ),
    )


if __name__ == "__main__":
    main()
