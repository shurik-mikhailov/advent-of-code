from get_input_data import get_input_data


def part_one(input_data: str):
    parts = input_data.split("\n\n")
    shapes = [p for p in parts if "#" in p]
    regions = parts[6].strip().splitlines()

    sharps = [s.count("#") for s in shapes]

    res = 0
    for r in regions:
        x, y = map(int, r.split(": ")[0].split("x"))
        nums = list(map(int, r.split(": ")[1].split(" ")))
        
        total = 0
        for i, c in enumerate(sharps):
            total += c * nums[i]

        res += (total <= x * y)

    return res


data = get_input_data(year=2025, task_number=12)
print(f'part one: {part_one(input_data=data)}')
