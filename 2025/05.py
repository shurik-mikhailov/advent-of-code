from get_input_data import get_input_data


def part_one(input_data: str):
    ranges, ids = input_data.strip().split("\n\n")

    ranges = ranges.strip().splitlines()
    ranges = [tuple(map(int, line.split("-"))) for line in ranges]

    ids = ids.strip().splitlines()
    ids = [int(line) for line in ids]

    fresh = 0
    for i in ids:
        for a, b in ranges:
            if a <= i <= b:
                fresh += 1
                break
    return fresh


def part_two(input_data: str):
    ranges = input_data.strip().split("\n\n")[0].strip().splitlines()
    ranges = [tuple(map(int, line.split("-"))) for line in ranges]
    ranges.sort()

    merged = list()
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    total = 0
    for a, b in merged:
        total += b - a + 1

    return total


data = get_input_data(year=2025, task_number=5)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
