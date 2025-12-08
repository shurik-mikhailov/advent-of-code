from collections import defaultdict

from get_input_data import get_input_data


def part_one(input_data: str):
    grid = input_data.strip().splitlines()
    w, h = len(grid[0]), len(grid)

    start = (0, grid[0].index('S'))
    splits = 0
    rays = {start}

    while rays:
        new_rays = set()

        for y, x in rays:
            ny = y + 1
            if ny >= h:
                continue

            if grid[ny][x] == '.':
                new_rays.add((ny, x))
            elif grid[ny][x] == '^':
                splits += 1
                if x - 1 >= 0:
                    new_rays.add((ny, x - 1))
                if x + 1 <= w:
                    new_rays.add((ny, x + 1))
        rays = new_rays

    return splits


def part_two(input_data: str):
    grid = input_data.strip().splitlines()
    w, h = len(grid[0]), len(grid)
    start = (0, grid[0].index('S'))

    timelines = [defaultdict(int) for _ in range(h + 1)]
    timelines[start[0]][start[1]] = 1

    res = 0

    for y in range(start[0], h):
        for x, cnt in timelines[y].items():
            if cnt == 0:
                continue

            ny = y + 1
            if ny >= h:
                res += cnt
                continue

            if x < 0 or x > w:
                res += cnt
                continue

            if grid[ny][x] == '.':
                timelines[ny][x] += cnt

            elif grid[ny][x] == '^':
                if x - 1 >= 0:
                    timelines[ny][x - 1] += cnt
                if x + 1 < w:
                    timelines[ny][x + 1] += cnt
    return res


data = get_input_data(year=2025, task_number=7)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
