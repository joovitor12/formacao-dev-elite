from __future__ import annotations

from dataset import build_data
from pipeline import build_user_value_report


def main() -> None:
    users, events = build_data(total_users=6, events_per_user=4)
    report, operations = build_user_value_report(users, events)

    print("Relatorio (3 primeiros):")
    for row in report[:3]:
        print(row)

    print(f"\nOperacoes: {operations}")
    print(f"Users: {len(users)} | Events: {len(events)}")


if __name__ == "__main__":
    main()
