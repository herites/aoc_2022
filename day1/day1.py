def main() -> None:
    elf_dict = dict_from_input()
    most_cals = max(elf_dict.values())
    print("Biggus dickus: " + str(most_cals))
    print("Top3: " + str(get_top3(elf_dict)))


def dict_from_input() -> dict:
    with open("input.txt") as f:
        lines = f.readlines()
    elf_dict = {}
    elf_num = 1
    for i in lines:
        if i == "\n":
            elf_num += 1
        else:
            if elf_num not in elf_dict.keys():
                elf_dict[elf_num] = 0
            elf_dict[elf_num] += int(i)
    return elf_dict


def get_top3(elf_dict: dict) -> dict:
    top3 = {}
    for i in range(3):
        top_elf = max(elf_dict, key=elf_dict.get)
        top3[top_elf] = elf_dict.pop(top_elf)
    return sum(top3.values())


if __name__ == "__main__":
    main()
