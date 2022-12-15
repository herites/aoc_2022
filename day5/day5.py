"""
    [P]                 [Q]     [T]
[F] [N]             [P] [L]     [M]
[H] [T] [H]         [M] [H]     [Z]
[M] [C] [P]     [Q] [R] [C]     [J]
[T] [J] [M] [F] [L] [G] [R]     [Q]
[V] [G] [D] [V] [G] [D] [N] [W] [L]
[L] [Q] [S] [B] [H] [B] [M] [L] [D]
[D] [H] [R] [L] [N] [W] [G] [C] [R]
 1   2   3   4   5   6   7   8   9 
"""


def main():
    instructions = load_input()[10:]
    global CRATE_LAYOUT
    CRATE_LAYOUT = get_initial_crate_layout(load_input()[:10])
    for instruction in instructions:
        move_crates(instruction)
    answer = ""
    for i in CRATE_LAYOUT.values():
        answer += i[-1]
    print(answer)


def get_initial_crate_layout(initial_layout: list[str]) -> dict[int, list[str]]:
    crate_layout = {x: [] for x in range(1, 10)}
    crate_indices = []
    for i in range(1, 10):
        crate_indices.append(int(initial_layout[8].index(str(i))))
    for line in initial_layout[:-2]:
        column = 1
        for index in crate_indices:
            if line[index] != " ":
                crate_layout[column].insert(0, line[index])
            column += 1
    return crate_layout


def move_crates(instruction: str):
    actions = ["crate_count", "from", "to"]
    nums = []
    for i in instruction.split(" "):
        if i.isnumeric():
            nums.append(int(i))
    instruction = dict(zip(actions, nums))
    for i in range(instruction["crate_count"]):
        popped = CRATE_LAYOUT[instruction["from"]].pop()
        CRATE_LAYOUT[instruction["to"]].append(popped)


def load_input(file: str = "input.txt") -> list[str]:
    with open(file, "r") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return lines


if __name__ == "__main__":
    main()
