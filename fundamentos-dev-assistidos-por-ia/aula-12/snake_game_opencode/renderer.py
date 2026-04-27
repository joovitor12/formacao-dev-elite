from __future__ import annotations

from snake_logic import GameState


GRID_CHAR = "+"
H_BORDER = "-"
V_BORDER = "|"
SNAKE_HEAD = "O"
SNAKE_BODY = "o"
FOOD_CHAR = "*"
EMPTY_CHAR = " "


COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_BOLD = "\033[1m"
COLOR_BRIGHT_GREEN = "\033[32m"
COLOR_BRIGHT_YELLOW = "\033[93m"
COLOR_BRIGHT_RED = "\033[91m"


COLOR_ENABLED = True


def _color(text: str, color: str) -> str:
    if COLOR_ENABLED:
        return f"{color}{text}{COLOR_RESET}"
    return text


def enable_colors(enabled: bool = True) -> None:
    global COLOR_ENABLED
    COLOR_ENABLED = enabled


def get_snake_head_char(x: int, y: int, state: GameState) -> str:
    return _color(SNAKE_HEAD, COLOR_BOLD + COLOR_GREEN)


def get_snake_body_char(x: int, y: int, state: GameState, body_index: int) -> str:
    intensity = max(255 - (body_index * 20), 100)
    green = f"\033[38;2;0;{intensity};0m"
    return _color(SNAKE_BODY, green)


def get_food_char(x: int, y: int, state: GameState) -> str:
    return _color(FOOD_CHAR, COLOR_RED)


def render(state: GameState) -> str:
    lines = []
    lines.append(
        _color(
            f"  SNAKE GAME  |  Score: {_color(str(state.score), COLOR_YELLOW)}  |  High: ?",
            COLOR_CYAN,
        )
    )
    lines.append("")

    border = _color(H_BORDER * (state.width * 2 + 2), COLOR_CYAN)
    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)}{border}{_color(V_BORDER, COLOR_CYAN)}"
    )

    food_set = {state.food} if not state.game_over else set()
    snake_set = set(state.snake)

    for y in range(state.height):
        row_cells = []
        for x in range(state.width):
            pos = (x, y)
            if pos == state.snake[0]:
                row_cells.append(get_snake_head_char(x, y, state))
            elif pos in snake_set:
                idx = state.snake.index(pos)
                row_cells.append(get_snake_body_char(x, y, state, idx))
            elif pos == state.food:
                row_cells.append(get_food_char(x, y, state))
            else:
                row_cells.append(_color(EMPTY_CHAR, COLOR_RESET))

        row_str = "".join(row_cells)
        lines.append(
            f"{_color(V_BORDER, COLOR_CYAN)} {row_str} {_color(V_BORDER, COLOR_CYAN)}"
        )

    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)}{border}{_color(V_BORDER, COLOR_CYAN)}"
    )
    lines.append("")
    lines.append(
        _color(
            "Controls: Arrow keys or WASD to move | P to pause | Q to quit", COLOR_RESET
        )
    )

    return "\n".join(lines)


def render_paused(state: GameState) -> str:
    lines = render(state).split("\n")
    pause_msg = _color("=== PAUSED ===", COLOR_YELLOW)
    lines[3] = (
        f"{_color(V_BORDER, COLOR_CYAN)} {pause_msg:^{state.width * 2}} {_color(V_BORDER, COLOR_CYAN)}"
    )
    return "\n".join(lines)


def render_game_over(state: GameState, player_name: str = "") -> str:
    lines = []
    msg = "GAME OVER!"
    lines.append(
        _color(
            f"  SNAKE GAME  |  Final Score: {_color(str(state.score), COLOR_YELLOW)}",
            COLOR_RED,
        )
    )
    lines.append("")

    border = _color(H_BORDER * (state.width * 2 + 2), COLOR_CYAN)
    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)}{border}{_color(V_BORDER, COLOR_CYAN)}"
    )

    msg = f"GAME OVER! Score: {state.score}"
    if player_name:
        msg = f"{player_name}: {state.score}"
    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)} {msg:^{state.width * 2}} {_color(V_BORDER, COLOR_CYAN)}"
    )

    msg2 = "Press ENTER to save score or Q to quit"
    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)} {msg2:^{state.width * 2}} {_color(V_BORDER, COLOR_CYAN)}"
    )

    lines.append(
        f"{_color(V_BORDER, COLOR_CYAN)}{border}{_color(V_BORDER, COLOR_CYAN)}"
    )
    lines.append("")

    return "\n".join(lines)


def render_high_scores(scores: list, current_score: int = 0) -> str:
    lines = []
    lines.append(_color("=" * 30, COLOR_CYAN))
    lines.append(_color("   HIGH SCORES   ", COLOR_BOLD + COLOR_YELLOW))
    lines.append(_color("=" * 30, COLOR_CYAN))

    for i, entry in enumerate(scores, 1):
        marker = ""
        if current_score and entry.score == current_score:
            marker = _color(" <- YOU!", COLOR_GREEN)
        score_str = f"{i:2}. {entry.player_name:<10} {entry.score:>4} pts{marker}"
        lines.append(_color(score_str, COLOR_RESET))

    if not scores:
        lines.append(_color("No scores yet!", COLOR_YELLOW))

    lines.append(_color("=" * 30, COLOR_CYAN))
    return "\n".join(lines)


def render_welcome() -> str:
    lines = []
    lines.append(_color("=" * 40, COLOR_CYAN))
    lines.append(
        _color("        WELCOME TO SNAKE GAME        ", COLOR_BOLD + COLOR_GREEN)
    )
    lines.append(_color("=" * 40, COLOR_CYAN))
    lines.append("")
    lines.append(
        _color(
            f"{SNAKE_HEAD} Snake Head   {SNAKE_BODY} Snake Body   {FOOD_CHAR} Food",
            COLOR_RESET,
        )
    )
    lines.append("")
    lines.append(_color("Controls:", COLOR_BOLD))
    lines.append("  Arrow Keys / WASD - Move")
    lines.append("  P - Pause/Resume")
    lines.append("  Q - Quit Game")
    lines.append("")
    lines.append(_color("=" * 40, COLOR_CYAN))
    return "\n".join(lines)
