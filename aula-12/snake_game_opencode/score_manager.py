from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


SCORES_FILE = "snake_scores.json"
MAX_TOP_SCORES = 10


@dataclass
class ScoreEntry:
    player_name: str
    score: int
    date: str

    def to_dict(self) -> dict:
        return {"player_name": self.player_name, "score": self.score, "date": self.date}

    @classmethod
    def from_dict(cls, data: dict) -> ScoreEntry:
        return cls(
            player_name=data["player_name"],
            score=data["score"],
            date=data["date"],
        )


@dataclass
class ScoreManager:
    scores: list[ScoreEntry] = field(default_factory=list)
    file_path: Path = field(default_factory=lambda: Path(SCORES_FILE))

    def load(self) -> None:
        if not self.file_path.exists():
            self.scores = []
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.scores = [
                    ScoreEntry.from_dict(entry) for entry in data.get("scores", [])
                ]
        except (json.JSONDecodeError, KeyError, TypeError):
            self.scores = []

    def save(self) -> None:
        data = {"scores": [entry.to_dict() for entry in self.scores]}
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_score(self, player_name: str, score: int, date: str) -> int:
        entry = ScoreEntry(player_name=player_name, score=score, date=date)
        self.scores.append(entry)
        self.scores.sort(key=lambda x: x.score, reverse=True)
        self.scores = self.scores[:MAX_TOP_SCORES]
        self.save()
        return self.get_rank(score)

    def get_rank(self, score: int) -> int:
        sorted_scores = sorted([s.score for s in self.scores], reverse=True)
        if score == 0:
            return len(sorted_scores) + 1
        for i, s in enumerate(sorted_scores):
            if score >= s:
                return i + 1
        return len(sorted_scores) + 1

    def get_top_scores(self, count: int = MAX_TOP_SCORES) -> list[ScoreEntry]:
        return self.scores[:count]

    def is_high_score(self, score: int) -> bool:
        if len(self.scores) < MAX_TOP_SCORES:
            return score > 0
        return score > self.scores[-1].score

    def get_lowest_top_score(self) -> int:
        if not self.scores:
            return 0
        return self.scores[-1].score
