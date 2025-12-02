from get_input_data import get_input_data


def part_one():
    pos, count = 50, 0

    for l in input_data.strip().splitlines():
        d = l[0]
        val = int(l[1:])
        pos = (pos - val) % 100 if d == 'L' else (pos + val) % 100
        count += 1 if pos == 0 else 0

    return count


def part_two():
    pos, count = 50, 0

    for l in input_data.strip().splitlines():
        d = l[0]
        val = int(l[1:])
        step = 1 if d == 'R' else -1
        for _ in range(val):
            pos = (pos + step) % 100
            if pos == 0:
                count += 1

    return count


input_data = get_input_data(year=2025, task_number=1)
print(f'Part One: {part_one()}')
print(f'Part Two: {part_two()}')
