from random import Random
import unittest

try:
    from snake_game_codex.snake_logic import (
        DOWN,
        LEFT,
        RIGHT,
        UP,
        GameState,
        change_direction,
        create_initial_state,
        spawn_food,
        step,
        toggle_pause,
    )
except ModuleNotFoundError:
    from snake_logic import (
        DOWN,
        LEFT,
        RIGHT,
        UP,
        GameState,
        change_direction,
        create_initial_state,
        spawn_food,
        step,
        toggle_pause,
    )


class SnakeLogicTests(unittest.TestCase):
    def test_estado_inicial_tem_cobra_com_tres_segmentos(self) -> None:
        state = create_initial_state(12, 12, Random(1))

        self.assertEqual(len(state.snake), 3)
        self.assertEqual(state.direction, RIGHT)
        self.assertEqual(state.score, 0)
        self.assertFalse(state.game_over)
        self.assertNotIn(state.food, state.snake)

    def test_nao_permitem_reverter_direcao(self) -> None:
        state = create_initial_state(12, 12, Random(1))

        updated = change_direction(state, LEFT)

        self.assertEqual(updated.pending_direction, RIGHT)

    def test_movimento_avanca_a_cabeca(self) -> None:
        state = GameState(
            width=8,
            height=8,
            snake=((3, 3), (2, 3), (1, 3)),
            direction=RIGHT,
            pending_direction=DOWN,
            food=(0, 0),
        )

        moved = step(state, Random(1))

        self.assertEqual(moved.snake, ((3, 4), (3, 3), (2, 3)))
        self.assertEqual(moved.direction, DOWN)

    def test_comer_aumenta_pontuacao_e_tamanho(self) -> None:
        state = GameState(
            width=8,
            height=8,
            snake=((3, 3), (2, 3), (1, 3)),
            direction=RIGHT,
            pending_direction=RIGHT,
            food=(4, 3),
        )

        moved = step(state, Random(2))

        self.assertEqual(moved.score, 1)
        self.assertEqual(len(moved.snake), 4)
        self.assertEqual(moved.snake[0], (4, 3))
        self.assertNotIn(moved.food, moved.snake)

    def test_colisao_com_parede_encerra_jogo(self) -> None:
        state = GameState(
            width=5,
            height=5,
            snake=((4, 2), (3, 2), (2, 2)),
            direction=RIGHT,
            pending_direction=RIGHT,
            food=(0, 0),
        )

        moved = step(state, Random(1))

        self.assertTrue(moved.game_over)

    def test_colisao_com_corpo_encerra_jogo(self) -> None:
        state = GameState(
            width=6,
            height=6,
            snake=((2, 2), (3, 2), (3, 3), (2, 3), (1, 3)),
            direction=UP,
            pending_direction=DOWN,
            food=(0, 0),
        )

        moved = step(state, Random(1))

        self.assertTrue(moved.game_over)

    def test_spawn_food_escolhe_espaco_livre(self) -> None:
        food = spawn_food(3, 3, ((0, 0), (1, 0), (2, 0), (0, 1)), Random(1))

        self.assertNotIn(food, ((0, 0), (1, 0), (2, 0), (0, 1)))

    def test_pause_impede_avanco_ate_retomar(self) -> None:
        state = create_initial_state(12, 12, Random(1))
        paused = toggle_pause(state)

        self.assertTrue(paused.paused)
        self.assertEqual(step(paused, Random(1)), paused)


if __name__ == "__main__":
    unittest.main()
