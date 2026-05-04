"""Mostra tamanho da entrada vs contagem de operações do baseline."""

from __future__ import annotations

from dataset import build_events
from metrics import summarize_points_by_user


def main() -> None:
    events = build_events(user_count=25, events_per_user=16)
    totals, operations = summarize_points_by_user(events)
    print(f"eventos={len(events)} usuarios_no_resultado={len(totals)} operacoes_contadas={operations}")


if __name__ == "__main__":
    main()
