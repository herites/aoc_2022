import csv


def main() -> None:
    with open("input.txt") as f:
        output = []
        for i in f.readlines():
            output.append({"opponent": i[0], "own": i[2]})

    with open("input.csv", "w", newline="") as f:
        fieldnames = ["opponent", "own"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    main()
