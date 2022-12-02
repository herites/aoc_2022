#%%
from dataclasses import dataclass
import pandas as pd


def main() -> None:

    plays = TheGame("input.csv")
    print(type(plays.data))


@dataclass
class TheGame:
    file_name: str
    opponent_play: str
    own_play: str

    def __post_init__(self):
        self.data = pd.read_csv(self.file_name)


if __name__ == "__main__":
    main()
