#%%
from dataclasses import dataclass
import pandas as pd

"""
X: Rock
Y: Paper
Z: Scissors
"""


def main() -> None:

    plays = TheGame("input.csv")
    plays.unencrypt_moves()
    plays.add_opponent_shape_score_rows()
    plays.set_opponent_total_shape_score()
    plays.add_own_shape_score_rows()
    plays.set_own_total_shape_score()

    print(plays.get_own_total_shape_score())
    print(plays.get_opponent_total_shape_score())
    print(plays.get_data().head())


@dataclass
class TheGame:
    file_name: str
    _own_total_score: int = 0
    _own_total_shape_score: int = 0

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

    def unencrypt_moves(self: pd.DataFrame):
        own_moves_key = {"X": "rock", "Y": "paper", "Z": "scissors"}
        opponent_moves_key = {"A": "rock", "B": "paper", "C": "scissors"}
        self._data["own_moves"] = self._data["own"].map(own_moves_key)
        self._data["opponent_moves"] = self._data["opponent"].map(opponent_moves_key)


if __name__ == "__main__":
    main()
