import string


def main() -> None:
    text = load_input("input.txt")
    solution = 0
    letter_values = generate_letter_values()
    start = 0
    step = 3
    for i in range(3, len(text) + step, step):
        curr = text[start:i]
        a = set(list(curr[0]))
        b = set(list(curr[1]))
        c = set(list(curr[2]))
        shared = "".join(a.intersection(b, c))
        solution += letter_values[shared]
        start += step
    print(solution)


def load_input(file: str) -> list[str]:
    with open(file, "r") as f:
        text = f.readlines()
    text_stripped = []
    for i in text:
        text_stripped.append(i.strip("\n"))
    return text_stripped


def generate_letter_values() -> dict:
    letter_values = {}
    for number, letter in enumerate(string.ascii_letters):
        letter_values[letter] = number + 1
    return letter_values


if __name__ == "__main__":
    main()
