from __future__ import annotations

from random import Random
import tkinter as tk

try:
    from snake_game_codex.snake_logic import (
        DIRECTION_BY_KEY,
        GRID_HEIGHT,
        GRID_WIDTH,
        GameState,
        create_initial_state,
        change_direction,
        step,
        toggle_pause,
    )
except ModuleNotFoundError:
    from snake_logic import (
        DIRECTION_BY_KEY,
        GRID_HEIGHT,
        GRID_WIDTH,
        GameState,
        create_initial_state,
        change_direction,
        step,
        toggle_pause,
    )


CELL_SIZE = 24
TICK_MS = 140
BACKGROUND = "#f4f4f4"
GRID_COLOR = "#d8d8d8"
SNAKE_COLOR = "#2f6f3e"
HEAD_COLOR = "#1f4d2a"
FOOD_COLOR = "#cf3c2f"
TEXT_COLOR = "#1b1b1b"


class SnakeGameApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Jogo da Cobrinha")
        self.root.configure(bg=BACKGROUND)
        self.rng = Random()
        self.state = create_initial_state(GRID_WIDTH, GRID_HEIGHT, self.rng)

        canvas_width = GRID_WIDTH * CELL_SIZE
        canvas_height = GRID_HEIGHT * CELL_SIZE

        self.frame = tk.Frame(root, bg=BACKGROUND, padx=16, pady=16)
        self.frame.pack()

        self.status_var = tk.StringVar()
        self.message_var = tk.StringVar()

        header = tk.Frame(self.frame, bg=BACKGROUND)
        header.pack(fill="x", pady=(0, 12))

        tk.Label(
            header,
            text="Jogo da Cobrinha",
            bg=BACKGROUND,
            fg=TEXT_COLOR,
            font=("Arial", 18, "bold"),
        ).pack(anchor="w")

        tk.Label(
            header,
            textvariable=self.status_var,
            bg=BACKGROUND,
            fg=TEXT_COLOR,
            font=("Arial", 11),
        ).pack(anchor="w", pady=(4, 0))

        self.canvas = tk.Canvas(
            self.frame,
            width=canvas_width,
            height=canvas_height,
            bg="white",
            highlightthickness=1,
            highlightbackground=GRID_COLOR,
        )
        self.canvas.pack()

        controls = tk.Frame(self.frame, bg=BACKGROUND)
        controls.pack(fill="x", pady=(12, 0))

        tk.Label(
            controls,
            text="Setas ou WASD para mover | Espaço para pausar | R para reiniciar",
            bg=BACKGROUND,
            fg=TEXT_COLOR,
            font=("Arial", 10),
        ).pack(anchor="w")

        tk.Label(
            controls,
            textvariable=self.message_var,
            bg=BACKGROUND,
            fg=TEXT_COLOR,
            font=("Arial", 10, "italic"),
        ).pack(anchor="w", pady=(6, 0))

        self.root.bind("<KeyPress>", self.on_key_press)

        self.draw()
        self.schedule_tick()

    def schedule_tick(self) -> None:
        self.root.after(TICK_MS, self.game_loop)

    def game_loop(self) -> None:
        self.state = step(self.state, self.rng)
        self.draw()
        self.schedule_tick()

    def on_key_press(self, event: tk.Event) -> None:
        key = event.keysym
        if key in ("space", "p", "P"):
            self.state = toggle_pause(self.state)
        elif key in ("r", "R"):
            self.restart()
        else:
            self.state = change_direction(self.state, DIRECTION_BY_KEY.get(key))

        self.draw()

    def restart(self) -> None:
        self.state = create_initial_state(GRID_WIDTH, GRID_HEIGHT, self.rng)

    def draw(self) -> None:
        self.canvas.delete("all")
        self.draw_grid(self.state)
        self.draw_food(self.state.food)
        self.draw_snake(self.state.snake)

        self.status_var.set(f"Pontuacao: {self.state.score}")
        if self.state.game_over:
            self.message_var.set("Fim de jogo. Pressione R para reiniciar.")
        elif self.state.paused:
            self.message_var.set("Jogo pausado. Pressione Espaço para continuar.")
        else:
            self.message_var.set("")

    def draw_grid(self, state: GameState) -> None:
        width_px = state.width * CELL_SIZE
        height_px = state.height * CELL_SIZE
        for x in range(0, width_px, CELL_SIZE):
            self.canvas.create_line(x, 0, x, height_px, fill=GRID_COLOR)
        for y in range(0, height_px, CELL_SIZE):
            self.canvas.create_line(0, y, width_px, y, fill=GRID_COLOR)

    def draw_food(self, food: tuple[int, int]) -> None:
        self.draw_cell(food, FOOD_COLOR, padding=4)

    def draw_snake(self, snake: tuple[tuple[int, int], ...]) -> None:
        for index, segment in enumerate(snake):
            color = HEAD_COLOR if index == 0 else SNAKE_COLOR
            self.draw_cell(segment, color, padding=2)

    def draw_cell(self, position: tuple[int, int], color: str, padding: int) -> None:
        x, y = position
        x1 = x * CELL_SIZE + padding
        y1 = y * CELL_SIZE + padding
        x2 = (x + 1) * CELL_SIZE - padding
        y2 = (y + 1) * CELL_SIZE - padding
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


def main() -> None:
    root = tk.Tk()
    SnakeGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
