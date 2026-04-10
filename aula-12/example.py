from __future__ import annotations

import random
import tkinter as tk

from snake_game import (
    DIRECTION_BY_KEY,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    create_initial_state,
    queue_direction,
    step_state,
)


CELL_SIZE = 28
GRID_WIDTH = 16
GRID_HEIGHT = 16
TICK_MS = 130

BG_COLOR = "#1a1a2e"
GRID_COLOR = "#1f2040"
SNAKE_COLOR = "#4ecca3"
HEAD_COLOR = "#2ecc71"
FOOD_COLOR = "#e94560"
TEXT_COLOR = "#eeeeee"
PANEL_COLOR = "#16213e"
BORDER_COLOR = "#4ecca3"
OVERLAY_BG = "#0a0a1a"

CANVAS_W = GRID_WIDTH * CELL_SIZE
CANVAS_H = GRID_HEIGHT * CELL_SIZE


class SnakeApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Snake")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.rng = random.Random()
        self.state = create_initial_state(GRID_WIDTH, GRID_HEIGHT, rng=self.rng)
        self.job_id: str | None = None
        self.paused = False
        self.high_score = 0

        container = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
        container.pack()

        # Header panel
        header = tk.Frame(container, bg=PANEL_COLOR, padx=14, pady=10)
        header.pack(fill="x", pady=(0, 10))

        self.score_var = tk.StringVar(value="Score: 0")
        self.high_score_var = tk.StringVar(value="Best: 0")
        self.status_var = tk.StringVar(value="Running")

        tk.Label(header, textvariable=self.score_var, bg=PANEL_COLOR, fg=SNAKE_COLOR,
                 font=("Consolas", 12, "bold")).pack(side="left")
        tk.Label(header, textvariable=self.status_var, bg=PANEL_COLOR, fg=TEXT_COLOR,
                 font=("Consolas", 11)).pack(side="left", padx=16)
        tk.Label(header, textvariable=self.high_score_var, bg=PANEL_COLOR, fg="#f0a500",
                 font=("Consolas", 12, "bold")).pack(side="right")

        # Canvas with teal border
        canvas_frame = tk.Frame(container, bg=BORDER_COLOR, padx=2, pady=2)
        canvas_frame.pack()

        self.canvas = tk.Canvas(
            canvas_frame,
            width=CANVAS_W,
            height=CANVAS_H,
            bg=BG_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack()

        # Controls bar
        controls = tk.Frame(container, bg=BG_COLOR)
        controls.pack(fill="x", pady=(10, 0))

        tk.Label(controls, text="\u2190 \u2192 \u2191 \u2193  WASD  |  Space = pause",
                 bg=BG_COLOR, fg="#666688", font=("Consolas", 10)).pack(side="left")

        tk.Button(
            controls, text="Restart", command=self.restart,
            bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Consolas", 10, "bold"),
            relief="flat", padx=12, pady=5, cursor="hand2",
            activebackground=SNAKE_COLOR, activeforeground=BG_COLOR, bd=0,
        ).pack(side="right")

        # D-pad buttons
        dpad = tk.Frame(container, bg=BG_COLOR)
        dpad.pack(pady=(10, 0))

        btn_kw = dict(
            bg=PANEL_COLOR, fg=TEXT_COLOR, font=("Consolas", 11, "bold"),
            relief="flat", padx=16, pady=8, cursor="hand2",
            activebackground=SNAKE_COLOR, activeforeground=BG_COLOR, bd=0,
        )
        tk.Button(dpad, text="\u25b2", command=lambda: self.handle_direction(UP), **btn_kw).grid(row=0, column=1, padx=3, pady=3)
        tk.Button(dpad, text="\u25c4", command=lambda: self.handle_direction(LEFT), **btn_kw).grid(row=1, column=0, padx=3, pady=3)
        tk.Button(dpad, text="\u25bc", command=lambda: self.handle_direction(DOWN), **btn_kw).grid(row=1, column=1, padx=3, pady=3)
        tk.Button(dpad, text="\u25ba", command=lambda: self.handle_direction(RIGHT), **btn_kw).grid(row=1, column=2, padx=3, pady=3)

        root.bind("<KeyPress>", self.on_keypress)
        self.render()
        self.schedule_tick()

    def on_keypress(self, event: tk.Event) -> None:
        if event.keysym == "space":
            self.toggle_pause()
            return
        direction = DIRECTION_BY_KEY.get(event.keysym)
        if direction is None and event.char:
            direction = DIRECTION_BY_KEY.get(event.char)
        if direction is not None:
            self.handle_direction(direction)

    def handle_direction(self, direction: tuple[int, int]) -> None:
        self.state = queue_direction(self.state, direction)

    def toggle_pause(self) -> None:
        if self.state.game_over:
            return
        self.paused = not self.paused
        if self.paused and self.job_id is not None:
            self.root.after_cancel(self.job_id)
            self.job_id = None
        elif not self.paused and self.job_id is None:
            self.schedule_tick()
        self.render()

    def restart(self) -> None:
        if self.job_id is not None:
            self.root.after_cancel(self.job_id)
            self.job_id = None
        self.paused = False
        self.state = create_initial_state(GRID_WIDTH, GRID_HEIGHT, rng=self.rng)
        self.render()
        self.schedule_tick()

    def schedule_tick(self) -> None:
        if not self.paused and not self.state.game_over:
            self.job_id = self.root.after(TICK_MS, self.tick)

    def tick(self) -> None:
        self.job_id = None
        self.state = step_state(self.state, rng=self.rng)
        if self.state.score > self.high_score:
            self.high_score = self.state.score
        self.render()
        self.schedule_tick()

    def render(self) -> None:
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_food()
        self.draw_snake()
        self.score_var.set(f"Score: {self.state.score}")
        self.high_score_var.set(f"Best: {self.high_score}")
        if self.state.won:
            self.status_var.set("You Win!")
            self._draw_overlay("YOU WIN!", "#f0a500", "Press Restart to play again")
        elif self.state.game_over:
            self.status_var.set("Game Over")
            self._draw_overlay("GAME OVER", FOOD_COLOR, "Press Restart to play again")
        elif self.paused:
            self.status_var.set("Paused")
            self._draw_overlay("PAUSED", TEXT_COLOR, "Press Space to resume")
        else:
            self.status_var.set("Running")

    def _draw_overlay(self, message: str, color: str, sub: str) -> None:
        cx = CANVAS_W // 2
        cy = CANVAS_H // 2
        self.canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H,
                                     fill=OVERLAY_BG, stipple="gray50", outline="")
        self.canvas.create_rectangle(cx - 110, cy - 36, cx + 110, cy + 36,
                                     fill=PANEL_COLOR, outline=color, width=2)
        self.canvas.create_text(cx, cy - 10, text=message, fill=color,
                                font=("Consolas", 18, "bold"))
        self.canvas.create_text(cx, cy + 16, text=sub, fill="#aaaaaa",
                                font=("Consolas", 9))

    def draw_grid(self) -> None:
        for x in range(GRID_WIDTH + 1):
            offset = x * CELL_SIZE
            self.canvas.create_line(offset, 0, offset, CANVAS_H, fill=GRID_COLOR)
        for y in range(GRID_HEIGHT + 1):
            offset = y * CELL_SIZE
            self.canvas.create_line(0, offset, CANVAS_W, offset, fill=GRID_COLOR)

    def draw_food(self) -> None:
        x, y = self.state.food
        cx = x * CELL_SIZE + CELL_SIZE // 2
        cy = y * CELL_SIZE + CELL_SIZE // 2
        r = CELL_SIZE // 2 - 3
        self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                fill=FOOD_COLOR, outline="")
        hr = max(2, r // 3)
        self.canvas.create_oval(cx - r + 2, cy - r + 2,
                                cx - r + 2 + hr, cy - r + 2 + hr,
                                fill="#ff8080", outline="")

    def draw_snake(self) -> None:
        snake = self.state.snake
        for i in range(len(snake) - 1):
            self._draw_connector(snake[i], snake[i + 1])
        for index, segment in enumerate(snake):
            color = HEAD_COLOR if index == 0 else SNAKE_COLOR
            self._draw_segment(segment, color)
        if snake:
            self._draw_eyes(snake[0], self.state.direction)

    def _draw_segment(self, position: tuple[int, int], color: str) -> None:
        x, y = position
        inset = 3
        left = x * CELL_SIZE + inset
        top = y * CELL_SIZE + inset
        right = left + CELL_SIZE - inset * 2
        bottom = top + CELL_SIZE - inset * 2
        self.canvas.create_oval(left, top, right, bottom, fill=color, outline="")

    def _draw_connector(self, a: tuple[int, int], b: tuple[int, int]) -> None:
        ax, ay = a
        bx, by = b
        inset = 3
        if ax == bx:  # vertical neighbors
            left = ax * CELL_SIZE + inset
            right = ax * CELL_SIZE + CELL_SIZE - inset
            top = min(ay, by) * CELL_SIZE + CELL_SIZE // 2
            bottom = max(ay, by) * CELL_SIZE + CELL_SIZE // 2
        else:  # horizontal neighbors
            top = ay * CELL_SIZE + inset
            bottom = ay * CELL_SIZE + CELL_SIZE - inset
            left = min(ax, bx) * CELL_SIZE + CELL_SIZE // 2
            right = max(ax, bx) * CELL_SIZE + CELL_SIZE // 2
        self.canvas.create_rectangle(left, top, right, bottom, fill=SNAKE_COLOR, outline="")

    def _draw_eyes(self, head: tuple[int, int], direction: tuple[int, int]) -> None:
        x, y = head
        cx = x * CELL_SIZE + CELL_SIZE // 2
        cy = y * CELL_SIZE + CELL_SIZE // 2
        dx, dy = direction
        r = 2
        if dx == 0:  # moving up or down
            eye1 = (cx - 4, cy + dy * 5)
            eye2 = (cx + 4, cy + dy * 5)
        else:  # moving left or right
            eye1 = (cx + dx * 5, cy - 4)
            eye2 = (cx + dx * 5, cy + 4)
        for ex, ey in [eye1, eye2]:
            self.canvas.create_oval(ex - r, ey - r, ex + r, ey + r,
                                    fill="#ffffff", outline="")


def main() -> None:
    root = tk.Tk()
    SnakeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
