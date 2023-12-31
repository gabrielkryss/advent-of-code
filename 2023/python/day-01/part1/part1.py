from pathlib import Path


def read_data(path: Path) -> list:
    """Read line data."""
    with path.open("r") as f:
        return [i.strip() for i in f.readlines()]


def parse(data: list[str]) -> list[int]:
    result = []
    for row in data:
        digits = [int(r) for r in row if r.isdigit()]
        # 10 first digit + last digit
        result.append(digits[0] * 10 + digits[-1])
    return result


def part1(data: list[str]) -> int:
    return sum(parse(data))


def translate_digits(data: list[str]) -> list[str]:
    result = []
    for row in data:
        for i, a in enumerate(
            (
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ),
            1,
        ):
            # replace matches by: first letter, number, last letter
            row = row.replace(a, f"{a[0]}{i}{a[-1]}")
        result.append(row)
    return result


def part2(data: list[str]) -> int:
    return part1(translate_digits(data))


if __name__ == "__main__":
    sdata = read_data(Path(f"./inputs\/sample.txt"))
    indata = read_data(Path(f"./inputs\/input.txt"))

    print("PART 1")
    print(f"\texample: {part1(sdata)}")
    print(f"\tinput: {part1(indata)}")
