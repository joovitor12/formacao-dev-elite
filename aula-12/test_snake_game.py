from __future__ import annotations

import random
import unittest

from snake_game import DOWN, LEFT, RIGHT, UP, GameState, create_initial_state, queue_direction, spawn_food, step_state


class SnakeGameTests(unittest.TestCase):
    def test_queue_direction_ignores_reverse_turn(self) -> None:
        state = create_initial_state()

        next_state = queue_direction(state, LEFT)

        self.assertEqual(next_state.pending_direction, RIGHT)

    def test_step_moves_snake_forward(self) -> None:
        state = create_initial_state()

        next_state = step_state(state)

        self.assertEqual(next_state.snake[0], (state.head[0] + 1, state.head[1]))
        self.assertEqual(len(next_state.snake), len(state.snake))

    def test_step_grows_and_scores_when_eating(self) -> None:
        state = GameState(
            width=6,
            height=6,
            snake=((2, 2), (1, 2), (0, 2)),
            direction=RIGHT,
            pending_direction=RIGHT,
            food=(3, 2),
        )

        next_state = step_state(state, rng=random.Random(7))

        self.assertEqual(next_state.score, 1)
        self.assertEqual(len(next_state.snake), 4)
        self.assertEqual(next_state.snake[0], (3, 2))
        self.assertNotIn(next_state.food, next_state.snake)

    def test_wall_collision_ends_game(self) -> None:
        state = GameState(
            width=4,
            height=4,
            snake=((3, 1), (2, 1), (1, 1)),
            direction=RIGHT,
            pending_direction=RIGHT,
            food=(0, 0),
        )

        next_state = step_state(state)

        self.assertTrue(next_state.game_over)

    def test_self_collision_ends_game(self) -> None:
        state = GameState(
            width=5,
            height=5,
            snake=((2, 2), (2, 3), (1, 3), (1, 2), (1, 1), (2, 1)),
            direction=UP,
            pending_direction=LEFT,
            food=(4, 4),
        )

        next_state = step_state(state)

        self.assertTrue(next_state.game_over)

    def test_spawn_food_uses_only_open_cells(self) -> None:
        food = spawn_food(2, 2, ((0, 0), (1, 0), (0, 1)), rng=random.Random(1))

        self.assertEqual(food, (1, 1))

    def test_winning_fill_marks_game_over(self) -> None:
        state = GameState(
            width=2,
            height=2,
            snake=((1, 0), (0, 0), (0, 1)),
            direction=DOWN,
            pending_direction=DOWN,
            food=(1, 1),
            score=3,
        )

        next_state = step_state(state)

        self.assertTrue(next_state.game_over)
        self.assertTrue(next_state.won)
        self.assertEqual(next_state.score, 4)


if __name__ == "__main__":
    unittest.main()
