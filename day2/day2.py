#%%
from dataclasses import dataclass
import pandas as pd
import numpy as np

"""
X: Rock
Y: Paper
Z: Scissors
"""


def main() -> None:

    plays = TheGame("input.csv")

    plays.add_opponent_shape_score_rows()
    plays.set_opponent_total_shape_score()

    plays.add_own_shape_score_rows()
    plays.set_own_total_shape_score()

    plays.unencrypt_moves()
    plays.calculate_moves()

    plays.add_own_play_score_rows()
    plays.set_own_total_play_score()

    plays.add_own_total_score_rows()
    plays.set_own_total_score()

    print(plays.get_own_total_score())
    print(plays.get_data().head(10))


@dataclass
class TheGame:
    file_name: str
    _own_total_score: int = 0
    _own_total_shape_score: int = 0
    _own_total_play_score: int = 0

    def __post_init__(self):
        self._data = pd.read_csv(self.file_name)

    def get_data(self) -> pd.DataFrame:
        return self._data

    def add_own_shape_score_rows(self) -> None:
        shape_key = {"X": 1, "Y": 2, "Z": 3}
        self._data["own_shape_score"] = self._data["own"].map(shape_key)

    def set_own_total_shape_score(self) -> None:
        self._own_shape_score = self._data["own_shape_score"].sum()

    def get_own_total_shape_score(self) -> int:
        return self._own_shape_score

    def add_opponent_shape_score_rows(self) -> None:
        shape_key = {"A": 1, "B": 2, "C": 3}
        self._data["opponent_shape_score"] = self._data["opponent"].map(shape_key)

    def set_opponent_total_shape_score(self) -> None:
        self._opponent_shape_score = self._data["opponent_shape_score"].sum()

    def get_opponent_total_shape_score(self) -> int:
        return self._opponent_shape_score

    def unencrypt_moves(self: pd.DataFrame) -> None:
        own_moves_key = {"X": "rock", "Y": "paper", "Z": "scissors"}
        opponent_moves_key = {"A": "rock", "B": "paper", "C": "scissors"}
        self._data["own_moves"] = self._data["own"].map(own_moves_key)
        self._data["opponent_moves"] = self._data["opponent"].map(opponent_moves_key)

    def calculate_moves(self) -> None:
        condlist = [
            self._data["opponent_moves"] == self._data["own_moves"],
            (self._data["opponent_moves"] == "scissors")
            & (self._data["own_moves"] == "rock"),
            (self._data["opponent_moves"] == "scissors")
            & (self._data["own_moves"] == "paper"),
            (self._data["opponent_moves"] == "rock")
            & (self._data["own_moves"] == "paper"),
            (self._data["opponent_moves"] == "rock")
            & (self._data["own_moves"] == "scissors"),
            (self._data["opponent_moves"] == "paper")
            & (self._data["own_moves"] == "scissors"),
            (self._data["opponent_moves"] == "paper")
            & (self._data["own_moves"] == "rock"),
        ]
        choicelist = [
            "draw",
            "player",
            "opponent",
            "player",
            "opponent",
            "player",
            "opponent",
        ]
        self._data["move_winner"] = np.select(condlist, choicelist)

    def add_own_play_score_rows(self) -> None:
        key = {"player": 6, "draw": 3, "opponent": 0}
        self._data["own_play_score"] = self._data["move_winner"].map(key)

    def set_own_total_play_score(self) -> None:
        self._own_total_play_score = self._data["own_play_score"].sum()

    def get_own_total_play_score(self) -> int:
        return self._own_total_play_score

    def add_own_total_score_rows(self) -> None:
        self._data["own_total_score"] = (
            self._data["own_shape_score"] + self._data["own_play_score"]
        )

    def set_own_total_score(self) -> None:
        self._own_total_score = self._data["own_total_score"].sum()

    def get_own_total_score(self) -> int:
        return self._own_total_score


if __name__ == "__main__":
    main()
