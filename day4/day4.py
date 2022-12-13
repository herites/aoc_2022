def main() -> None:
    text = load_input("input.txt")
    count = 0
    for line, i in enumerate(text):
        # if True in compare_ranges(_get_pairs(i)):
        #     count += 1
        print(line + 1, compare_ranges(_get_pairs(i)))
        if True in compare_ranges(_get_pairs(i)):
            count += 1
    print(count)


def compare_ranges(pair: tuple) -> bool:
    first_range = _get_edges(pair[0])
    second_range = _get_edges(pair[1])

    def _first_in_second(first_range, second_range):
        for i in first_range:
            return True if i in second_range else False

    def _second_in_first(first_range, second_range):
        for i in second_range:
            return True if i in first_range else False

    return _first_in_second(
        first_range, range(second_range[0], second_range[1] + 1)
    ), _second_in_first(range(first_range[0], first_range[1] + 1), second_range)


def _get_edges(text: str) -> list[int]:
    beginning = int(text.split("-")[0])
    end = int(text.split("-")[1])
    return beginning, end


def _get_pairs(text: str) -> list[int]:
    first = text.split(",")[0]
    second = text.split(",")[1]
    return first, second


def load_input(file: str) -> list[str]:
    with open(file, "r") as f:
        text = [x.strip() for x in f.readlines()]
    return text


if __name__ == "__main__":
    main()
