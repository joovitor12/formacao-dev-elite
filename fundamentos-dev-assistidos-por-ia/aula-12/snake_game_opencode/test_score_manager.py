import os
import tempfile
import unittest
from pathlib import Path

try:
    from snake_game_opencode.score_manager import (
        ScoreManager,
        ScoreEntry,
        MAX_TOP_SCORES,
    )
except ModuleNotFoundError:
    from score_manager import ScoreManager, ScoreEntry, MAX_TOP_SCORES


class ScoreManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".json"
        )
        self.temp_file.close()
        self.score_manager = ScoreManager(file_path=Path(self.temp_file.name))

    def tearDown(self) -> None:
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_add_score_updates_scores_list(self) -> None:
        self.score_manager.add_score("Alice", 100, "2024-01-01")

        self.assertEqual(len(self.score_manager.scores), 1)
        self.assertEqual(self.score_manager.scores[0].player_name, "Alice")
        self.assertEqual(self.score_manager.scores[0].score, 100)

    def test_scores_sorted_descending(self) -> None:
        self.score_manager.add_score("Bob", 50, "2024-01-01")
        self.score_manager.add_score("Alice", 100, "2024-01-01")
        self.score_manager.add_score("Charlie", 75, "2024-01-01")

        scores = [s.score for s in self.score_manager.scores]
        self.assertEqual(scores, [100, 75, 50])

    def test_max_scores_limit(self) -> None:
        for i in range(MAX_TOP_SCORES + 5):
            self.score_manager.add_score(f"Player{i}", i * 10, "2024-01-01")

        self.assertEqual(len(self.score_manager.scores), MAX_TOP_SCORES)
        self.assertEqual(self.score_manager.scores[0].score, (MAX_TOP_SCORES + 4) * 10)

    def test_save_and_load(self) -> None:
        self.score_manager.add_score("Test", 999, "2024-01-01")
        self.score_manager.save()

        new_manager = ScoreManager(file_path=Path(self.temp_file.name))
        new_manager.load()

        self.assertEqual(len(new_manager.scores), 1)
        self.assertEqual(new_manager.scores[0].score, 999)

    def test_get_top_scores_returns_correct_count(self) -> None:
        for i in range(5):
            self.score_manager.add_score(f"Player{i}", i * 10, "2024-01-01")

        top3 = self.score_manager.get_top_scores(3)

        self.assertEqual(len(top3), 3)
        self.assertEqual(top3[0].score, 40)

    def test_is_high_score_true_when_empty(self) -> None:
        self.assertTrue(self.score_manager.is_high_score(10))
        self.assertFalse(self.score_manager.is_high_score(0))

    def test_is_high_score_respects_limit(self) -> None:
        for i in range(MAX_TOP_SCORES):
            self.score_manager.add_score(f"P{i}", i + 1, "2024-01-01")

        self.assertFalse(self.score_manager.is_high_score(1))
        self.assertTrue(self.score_manager.is_high_score(MAX_TOP_SCORES + 1))

    def test_get_rank(self) -> None:
        self.score_manager.add_score("First", 100, "2024-01-01")
        self.score_manager.add_score("Second", 50, "2024-01-01")

        self.assertEqual(self.score_manager.get_rank(100), 1)
        self.assertEqual(self.score_manager.get_rank(75), 2)
        self.assertEqual(self.score_manager.get_rank(25), 3)

    def test_get_lowest_top_score_empty(self) -> None:
        self.assertEqual(self.score_manager.get_lowest_top_score(), 0)

    def test_get_lowest_top_score_with_scores(self) -> None:
        self.score_manager.add_score("A", 100, "2024-01-01")
        self.score_manager.add_score("B", 50, "2024-01-01")

        self.assertEqual(self.score_manager.get_lowest_top_score(), 50)


class ScoreEntryTests(unittest.TestCase):
    def test_to_dict(self) -> None:
        entry = ScoreEntry("Test", 100, "2024-01-01")
        data = entry.to_dict()

        self.assertEqual(data["player_name"], "Test")
        self.assertEqual(data["score"], 100)
        self.assertEqual(data["date"], "2024-01-01")

    def test_from_dict(self) -> None:
        data = {"player_name": "Test", "score": 100, "date": "2024-01-01"}
        entry = ScoreEntry.from_dict(data)

        self.assertEqual(entry.player_name, "Test")
        self.assertEqual(entry.score, 100)
        self.assertEqual(entry.date, "2024-01-01")


if __name__ == "__main__":
    unittest.main()
