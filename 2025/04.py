from get_input_data import get_input_data


def part_one(input_data: str):
    grid = input_data.strip().splitlines()

    h = len(grid)
    w = len(grid[0])

    close_pos = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    can_be = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != '@':
                continue
            adj = 0
            for di, dj in close_pos:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == '@':
                    adj += 1
            if adj < 4:
                can_be += 1

    return can_be


def part_two(input_data: str):
    grid = input_data.strip().splitlines()
    h = len(grid)
    w = len(grid[0])
    grid = [list(row) for row in grid]

    close_pos = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    removed = 0

    while True:
        remove = []
        for i in range(h):
            for j in range(w):
                if grid[i][j] != '@':
                    continue
                adj = 0
                for di, dj in close_pos:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == '@':
                        adj += 1
                if adj < 4:
                    remove.append((i, j))

        if not remove:
            break

        for i, j in remove:
            grid[i][j] = '.'
        removed += len(remove)

    return removed


data = get_input_data(year=2025, task_number=4)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
