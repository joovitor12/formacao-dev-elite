from __future__ import annotations

import os
import sys
from datetime import datetime
from random import Random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from snake_logic import (
    GameState,
    create_initial_state,
    step,
    change_direction,
    toggle_pause,
    DIRECTION_BY_KEY,
    GRID_WIDTH,
    GRID_HEIGHT,
)
from score_manager import ScoreManager
from renderer import (
    render,
    render_paused,
    render_game_over,
    render_high_scores,
    render_welcome,
    enable_colors,
)


class TerminalInput:
    @staticmethod
    def get_key() -> str:
        if os.name == "nt":
            import msvcrt

            ch = msvcrt.getch()
            if ch == b"\x00" or ch == b"\xe0":
                ch = msvcrt.getch()
                if ch == b"H":
                    return "Up"
                elif ch == b"P":
                    return "Down"
                elif ch == b"M":
                    return "Right"
                elif ch == b"K":
                    return "Left"
                return ""
            elif ch == b"\r":
                return "\r"
            elif ch == b"q" or ch == b"Q":
                return "q"
            elif ch == b"p" or ch == b"P":
                return "p"
            elif ch == b"s" or ch == b"S":
                return "s"
            try:
                return ch.decode("utf-8")
            except:
                return ""
        else:
            import tty
            import termios

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    seq = sys.stdin.read(2)
                    if seq == "[A":
                        return "Up"
                    elif seq == "[B":
                        return "Down"
                    elif seq == "[C":
                        return "Right"
                    elif seq == "[D":
                        return "Left"
                    return seq
                return ch
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    @staticmethod
    def get_line() -> str:
        return input().strip()


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def save_score_flow(score_manager: ScoreManager, score: int) -> str | None:
    if score == 0:
        return None

    if not score_manager.is_high_score(score):
        print(
            render_game_over(
                GameState(
                    GRID_WIDTH, GRID_HEIGHT, (), (0, 0), (0, 0), (0, 0), score, True
                ),
                "",
            )
        )
        print()
        print("Score not high enough for leaderboard.")
        print("Press ENTER to continue...")
        TerminalInput.get_line()
        return None

    print()
    print("=" * 40)
    print("  NEW HIGH SCORE! Enter your name:")
    print("=" * 40)
    print()
    player_name = TerminalInput.get_line()

    if not player_name:
        player_name = "Anonymous"

    player_name = player_name[:10]
    date = datetime.now().strftime("%Y-%m-%d")
    rank = score_manager.add_score(player_name, score, date)

    return player_name


def show_scores(score_manager: ScoreManager, current_score: int = 0) -> None:
    clear_screen()
    top_scores = score_manager.get_top_scores()
    print(render_high_scores(top_scores, current_score))
    print()
    print("Press ENTER to continue...")
    TerminalInput.get_line()


def game_loop(score_manager: ScoreManager, rng: Random | None = None) -> GameState:
    state = create_initial_state(GRID_WIDTH, GRID_HEIGHT, rng)
    running = True

    while running:
        clear_screen()

        if state.paused:
            print(render_paused(state))
            print()
            print("Press P to resume or Q to quit...")
        else:
            print(render(state))
            print()
            print("Press ENTER to move (or direction key)...")

        key = TerminalInput.get_key()
        key_upper = key.upper()

        if key_upper == "Q":
            running = False
        elif key_upper == "P":
            state = toggle_pause(state)
        elif key in DIRECTION_BY_KEY:
            state = change_direction(state, DIRECTION_BY_KEY[key])
        elif key == "\r" and not state.paused:
            state = step(state, rng)

        if state.game_over and key == "\r":
            saved_name = save_score_flow(score_manager, state.score)
            clear_screen()
            show_scores(score_manager, state.score)
            return state

    return state


def main() -> None:
    enable_colors(False)

    score_manager = ScoreManager()
    score_manager.load()

    while True:
        clear_screen()
        print(render_welcome())

        print()
        top = score_manager.get_top_scores(3)
        if top:
            print("Top 3 Scores:")
            for i, entry in enumerate(top, 1):
                print(f"  {i}. {entry.player_name}: {entry.score}")
        print()

        print("1 - Start Game")
        print("2 - View All Scores")
        print("3 - Quit")
        print()

        choice = input("Choose option: ").strip()

        if choice == "1":
            rng = Random()
            final_state = game_loop(score_manager, rng)
        elif choice == "2":
            show_scores(score_manager)
        elif choice == "3" or choice.lower() == "q":
            break
        else:
            print("Invalid option. Press ENTER to continue...")
            input()

    clear_screen()
    print(render_high_scores(score_manager.get_top_scores()))
    print()
    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
