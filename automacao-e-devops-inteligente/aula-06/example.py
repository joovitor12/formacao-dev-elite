"""Execute: python example.py"""

from __future__ import annotations

import merge_policy as policy


def main() -> None:
    print("dev 0 apr:", policy.pode_mergear("dev", 0, True))
    print("staging 1 apr:", policy.pode_mergear("staging", 1, True))
    print("prod 1 apr:", policy.pode_mergear("prod", 1, True))
    print("prod 2 apr:", policy.pode_mergear("prod", 2, True))


if __name__ == "__main__":
    main()
