def main() -> None:
    elf_dict = dict_from_input()
    print(max(elf_dict.values()))
    print(sum(sorted(elf_dict.values(), reverse=True)[:3]))


def dict_from_input() -> dict:
    with open("input.txt") as f:
        lines = f.readlines()
    elf_dict = {}
    current_elf = 1
    for i in lines:
        if i == "\n":  # doesn't account for first line being newline
            current_elf += 1
        else:
            if current_elf not in elf_dict.keys():
                elf_dict[current_elf] = 0
            elf_dict[current_elf] += int(i)
    return elf_dict


if __name__ == "__main__":
    main()
