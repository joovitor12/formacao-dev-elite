"""Demonstração rápida: carga fixa + tempo de parede + contagem de operações."""

from __future__ import annotations

from benchmark_harness import measure_wall_clock_ms
from dataset import build_observations
from stats_engine import aggregate_sum_by_group


def main() -> None:
    rows = build_observations(row_count=4000, group_count=120)

    def run_once():
        return aggregate_sum_by_group(rows)

    (_totals, ops), min_ms = measure_wall_clock_ms(run_once, repetitions=5, warmup=1)

    print(f"Linhas: {len(rows)}")
    print(f"Operações contadas (motor): {ops}")
    print(f"Tempo mínimo observado (ms): {min_ms:.3f}")


if __name__ == "__main__":
    main()
