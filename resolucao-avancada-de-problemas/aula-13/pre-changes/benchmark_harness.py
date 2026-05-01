"""Mesmo harness da raiz — benchmarks comparáveis só mudando stats_engine."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def measure_wall_clock_ms(
    fn: Callable[[], T], *, repetitions: int = 5, warmup: int = 1
) -> tuple[T, float]:
    for _ in range(warmup):
        fn()

    samples_ms: list[float] = []
    last_result: T | None = None
    for _ in range(repetitions):
        t0 = time.perf_counter()
        last_result = fn()
        samples_ms.append((time.perf_counter() - t0) * 1000.0)

    assert last_result is not None
    return last_result, min(samples_ms)
