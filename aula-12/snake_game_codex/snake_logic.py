from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import Iterable


GRID_WIDTH = 20
GRID_HEIGHT = 20

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTION_BY_KEY = {
    "Up": UP,
    "Down": DOWN,
    "Left": LEFT,
    "Right": RIGHT,
    "w": UP,
    "W": UP,
    "s": DOWN,
    "S": DOWN,
    "a": LEFT,
    "A": LEFT,
    "d": RIGHT,
    "D": RIGHT,
}


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
    paused: bool = False


def _is_opposite(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] == -b[0] and a[1] == -b[1]


def _available_cells(
    width: int, height: int, occupied: Iterable[tuple[int, int]]
) -> list[tuple[int, int]]:
    occupied_set = set(occupied)
    return [
        (x, y)
        for y in range(height)
        for x in range(width)
        if (x, y) not in occupied_set
    ]


def spawn_food(
    width: int,
    height: int,
    occupied: Iterable[tuple[int, int]],
    rng: Random | None = None,
) -> tuple[int, int]:
    cells = _available_cells(width, height, occupied)
    if not cells:
        raise ValueError("Nao ha espaco livre para gerar comida.")

    chooser = rng or Random()
    return cells[chooser.randrange(len(cells))]


def create_initial_state(
    width: int = GRID_WIDTH,
    height: int = GRID_HEIGHT,
    rng: Random | None = None,
) -> GameState:
    center_x = width // 2
    center_y = height // 2
    snake = (
        (center_x, center_y),
        (center_x - 1, center_y),
        (center_x - 2, center_y),
    )
    food = spawn_food(width, height, snake, rng)
    return GameState(
        width=width,
        height=height,
        snake=snake,
        direction=RIGHT,
        pending_direction=RIGHT,
        food=food,
    )


def change_direction(
    state: GameState, new_direction: tuple[int, int] | None
) -> GameState:
    if state.game_over or new_direction is None:
        return state

    reference = state.pending_direction or state.direction
    if _is_opposite(reference, new_direction):
        return state

    return GameState(
        width=state.width,
        height=state.height,
        snake=state.snake,
        direction=state.direction,
        pending_direction=new_direction,
        food=state.food,
        score=state.score,
        game_over=state.game_over,
        paused=state.paused,
    )


def toggle_pause(state: GameState) -> GameState:
    if state.game_over:
        return state

    return GameState(
        width=state.width,
        height=state.height,
        snake=state.snake,
        direction=state.direction,
        pending_direction=state.pending_direction,
        food=state.food,
        score=state.score,
        game_over=state.game_over,
        paused=not state.paused,
    )


def step(state: GameState, rng: Random | None = None) -> GameState:
    if state.game_over or state.paused:
        return state

    direction = state.pending_direction
    head_x, head_y = state.snake[0]
    next_head = (head_x + direction[0], head_y + direction[1])

    hit_wall = (
        next_head[0] < 0
        or next_head[0] >= state.width
        or next_head[1] < 0
        or next_head[1] >= state.height
    )
    hit_self = next_head in state.snake[:-1]
    if hit_wall or hit_self:
        return GameState(
            width=state.width,
            height=state.height,
            snake=state.snake,
            direction=direction,
            pending_direction=direction,
            food=state.food,
            score=state.score,
            game_over=True,
            paused=False,
        )

    ate_food = next_head == state.food
    next_snake = (next_head, *state.snake) if ate_food else (next_head, *state.snake[:-1])

    if ate_food and len(next_snake) == state.width * state.height:
        return GameState(
            width=state.width,
            height=state.height,
            snake=next_snake,
            direction=direction,
            pending_direction=direction,
            food=state.food,
            score=state.score + 1,
            game_over=True,
            paused=False,
        )

    next_food = (
        spawn_food(state.width, state.height, next_snake, rng) if ate_food else state.food
    )

    return GameState(
        width=state.width,
        height=state.height,
        snake=next_snake,
        direction=direction,
        pending_direction=direction,
        food=next_food,
        score=state.score + 1 if ate_food else state.score,
        game_over=False,
        paused=False,
    )
