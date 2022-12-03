import string


def main() -> None:
    text = load_input("input.txt")
    shared_letters = []
    for i in text:
        shared_letters.append(find_same_letter(i))

    print(get_solution(shared_letters))


def load_input(file: str) -> list[str]:
    with open(file, "r") as f:
        text = f.readlines()
    text_stripped = []
    for i in text:
        text_stripped.append(i.strip("\n"))
    return text_stripped


def find_same_letter(line: str) -> str:
    def slice_line(s: str) -> list:
        half = int(len(s) / 2)
        return [s[:half], s[half:]]

    parts = slice_line(line)
    return [x for x in parts[0] if x in parts[1]][0]


def get_solution(shared_letters: list) -> int:
    def generate_letter_values() -> dict:
        letter_values = {}
        for number, letter in enumerate(string.ascii_letters):
            letter_values[letter] = number + 1
        return letter_values

    letter_values = generate_letter_values()
    solution = 0
    for i in shared_letters:
        solution += letter_values[i]
    return solution


if __name__ == "__main__":
    main()
