from get_input_data import get_input_data


def part_one(input_data: str):
    ranges = input_data.strip().split(',')
    total = 0

    for r in ranges:
        a, b = map(int, r.split('-'))
        for i in range(a, b + 1):
            s = str(i)
            l = len(s)
            if l % 2 != 0:
                continue
            half = l // 2
            if s[:half] == s[half:]:
                total += i

    return total


def part_two(input_data: str):
    ranges = input_data.strip().split(',')
    total = 0

    for r in ranges:
        a, b = map(int, r.split('-'))
        for i in range(a, b + 1):
            s = str(i)
            l = len(s)
            found = False
            for k in range(1, l // 2 + 1):
                if l % k != 0:
                    continue
                if s == s[:k] * (l // k):
                    found = True
                    break
            if found:
                total += i

    return total


data = get_input_data(year=2025, task_number=2)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
