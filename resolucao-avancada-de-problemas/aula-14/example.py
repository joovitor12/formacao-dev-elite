"""Script curto: roda um caso e mostra resultado + operações."""

from __future__ import annotations

import time

from dataset import sample_values
from parity_sum import sum_even_numbers


def main() -> None:
    values = sample_values(20)
    start = time.perf_counter()
    total, ops = sum_even_numbers(values)
    elapsed_ms = (time.perf_counter() - start) * 1000.0

    print("Valores (primeiros 8):", values[:8])
    print("Soma dos pares:", total)
    print("Operações contadas:", ops)
    print(f"Tempo (uma execução, ms): {elapsed_ms:.4f}")


if __name__ == "__main__":
    main()
