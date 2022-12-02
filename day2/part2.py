from dataclasses import dataclass
import pandas as pd
import numpy as np


def main() -> None:
    plays = TheGame("input.csv")
    plays.decrypt()
    plays.calculate_own_move()
    plays.add_play_score_rows()
    plays.add_shape_score_rows()
    plays.play_score = "default"
    plays.shape_score = "default"
    plays.total_score = plays.play_score + plays.shape_score
    print(plays.total_score)


@dataclass
class TheGame:
    file_name: str
    _total_score: int = 0
    _shape_score: int = 0
    _play_score: int = 0

    def __post_init__(self):
        self._data = pd.read_csv(self.file_name)

    def get_data(self) -> pd.DataFrame:
        return self._data

    def decrypt(self: pd.DataFrame) -> None:
        own_moves_key = {"X": "loss", "Y": "draw", "Z": "win"}
        opponent_moves_key = {"A": "rock", "B": "paper", "C": "scissors"}
        self._data["opponent_move"] = self._data["opponent"].map(opponent_moves_key)
        self._data["expected_outcome"] = self._data["own"].map(own_moves_key)

    def calculate_own_move(self) -> None:
        conds = [
            (self._data["opponent_move"] == "scissors")
            & (self._data["expected_outcome"] == "loss"),
            (self._data["opponent_move"] == "scissors")
            & (self._data["expected_outcome"] == "win"),
            (self._data["opponent_move"] == "rock")
            & (self._data["expected_outcome"] == "loss"),
            (self._data["opponent_move"] == "rock")
            & (self._data["expected_outcome"] == "win"),
            (self._data["opponent_move"] == "paper")
            & (self._data["expected_outcome"] == "loss"),
            (self._data["opponent_move"] == "paper")
            & (self._data["expected_outcome"] == "win"),
            (self._data["opponent_move"] == "rock")
            & (self._data["expected_outcome"] == "draw"),
            (self._data["opponent_move"] == "paper")
            & (self._data["expected_outcome"] == "draw"),
            (self._data["opponent_move"] == "scissors")
            & (self._data["expected_outcome"] == "draw"),
        ]
        choices = [
            "paper",
            "rock",
            "scissors",
            "paper",
            "rock",
            "scissors",
            "rock",
            "paper",
            "scissors",
        ]
        self._data["own_move"] = np.select(condlist=conds, choicelist=choices)

    def add_play_score_rows(self) -> None:
        key = {"win": 6, "draw": 3, "loss": 0}
        self._data["play_score"] = self._data["expected_outcome"].map(key)

    @property
    def play_score(self) -> int:
        return self._play_score

    @play_score.setter
    def play_score(self, new_score) -> None:
        if new_score == "default":
            self._play_score = self._data["play_score"].sum()
        else:
            self._play_score = new_score

    def add_shape_score_rows(self) -> None:
        key = {"rock": 1, "paper": 2, "scissors": 3}
        self._data["shape_score"] = self._data["own_move"].map(key)

    @property
    def shape_score(self) -> int:
        return self._shape_score

    @shape_score.setter
    def shape_score(self, new_score) -> None:
        if new_score == "default":
            self._shape_score = self._data["shape_score"].sum()
        else:
            self._shape_score = new_score

    @property
    def total_score(self):
        return self._total_score

    @total_score.setter
    def total_score(self, new_score):
        self._total_score = new_score


if __name__ == "__main__":
    main()
