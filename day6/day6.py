def main() -> None:
    print(find_beginning(load_input()))


def find_beginning(text: str) -> int:
    chars_checked = 0
    unique_counter = 0
    start_marker = ""
    for i in text:
        chars_checked += 1
        if i in start_marker:
            start_marker = i
            unique_counter = 1
        if i not in start_marker:
            start_marker += i
            unique_counter += 1
        if unique_counter == 14:
            return chars_checked


def load_input(file: str = "input.txt") -> str:
    with open(file, "r") as f:
        text = f.read()
    return text


if __name__ == "__main__":
    main()
