import math

from get_input_data import get_input_data


def part_one(input_data: str) -> int:
    row1, row2, row3, row4, ops = input_data.strip().splitlines()

    row1 = [int(x.strip()) for x in row1.split()]
    row2 = [int(x.strip()) for x in row2.split()]
    row3 = [int(x.strip()) for x in row3.split()]
    row4 = [int(x.strip()) for x in row4.split()]
    ops = [x.strip() for x in ops.split()]

    res = 0
    for i in range(len(ops)):
        if ops[i] == "+":
            res += row1[i] + row2[i] + row3[i] + row4[i]
        else:
            res += row1[i] * row2[i] * row3[i] * row4[i]

    return res


def part_two(input_data: str):
    row1, row2, row3, row4, ops = input_data.splitlines()

    res = 0
    nums = []
    op = ""
    for i in range(len(ops) - 1, -1, -1):
        if ops[i] != " ":
            op = ops[i]
        if not row1[i] == row2[i] == row3[i] == row4[i] == " ":
            nums.append(int("".join([row1[i], row2[i], row3[i], row4[i]])))
        else:
            if op == "+":
                res += sum(nums)
            else:
                res += math.prod(nums)
            nums = []
            op = ""

    return res


data = get_input_data(year=2025, task_number=6)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
