from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, replace
import random
from typing import Final


UP: Final[tuple[int, int]] = (0, -1)
DOWN: Final[tuple[int, int]] = (0, 1)
LEFT: Final[tuple[int, int]] = (-1, 0)
RIGHT: Final[tuple[int, int]] = (1, 0)

DIRECTION_BY_KEY: Final[dict[str, tuple[int, int]]] = {
    "Up": UP,
    "w": UP,
    "W": UP,
    "Down": DOWN,
    "s": DOWN,
    "S": DOWN,
    "Left": LEFT,
    "a": LEFT,
    "A": LEFT,
    "Right": RIGHT,
    "d": RIGHT,
    "D": RIGHT,
}


def _is_opposite(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] == -b[0] and a[1] == -b[1]


@dataclass(frozen=True)
class GameState:
    width: int
    height: int
    snake: tuple[tuple[int, int], ...]
    direction: tuple[int, int]
    pending_direction: tuple[int, int]
    food: tuple[int, int]
    score: int = 0
    game_over: bool = False
    won: bool = False

    @property
    def head(self) -> tuple[int, int]:
        return self.snake[0]


def create_initial_state(
    width: int = 16,
    height: int = 16,
    *,
    rng: random.Random | None = None,
) -> GameState:
    center = (width // 2, height // 2)
    snake = (center, (center[0] - 1, center[1]), (center[0] - 2, center[1]))
    initial_direction = RIGHT
    food = spawn_food(width, height, snake, rng=rng)
    return GameState(
        width=width,
        height=height,
        snake=snake,
        direction=initial_direction,
        pending_direction=initial_direction,
        food=food,
    )


def queue_direction(state: GameState, direction: tuple[int, int]) -> GameState:
    if state.game_over:
        return state
    if _is_opposite(direction, state.direction):
        return state
    return replace(state, pending_direction=direction)


def step_state(state: GameState, *, rng: random.Random | None = None) -> GameState:
    if state.game_over:
        return state

    direction = state.pending_direction
    head_x, head_y = state.head
    next_head = (head_x + direction[0], head_y + direction[1])
    ate_food = next_head == state.food
    current_body = state.snake if ate_food else state.snake[:-1]

    if not (0 <= next_head[0] < state.width and 0 <= next_head[1] < state.height):
        return replace(state, direction=direction, game_over=True)

    if next_head in current_body:
        return replace(state, direction=direction, game_over=True)

    next_snake = (next_head, *state.snake)
    if not ate_food:
        next_snake = next_snake[:-1]

    won = len(next_snake) == state.width * state.height
    next_food = state.food
    next_score = state.score

    if ate_food:
        next_score += 1
        if not won:
            next_food = spawn_food(state.width, state.height, next_snake, rng=rng)

    return GameState(
        width=state.width,
        height=state.height,
        snake=next_snake,
        direction=direction,
        pending_direction=direction,
        food=next_food,
        score=next_score,
        game_over=won,
        won=won,
    )


def spawn_food(
    width: int,
    height: int,
    snake: Iterable[tuple[int, int]],
    *,
    rng: random.Random | None = None,
) -> tuple[int, int]:
    occupied = set(snake)
    open_cells = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if (x, y) not in occupied
    ]
    if not open_cells:
        raise ValueError("Cannot place food on a full board.")
    chooser = rng if rng is not None else random
    return chooser.choice(open_cells)
