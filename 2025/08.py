import math

from get_input_data import get_input_data


def find(val: int, parent: list) -> int:
    while parent[val] != val:
        parent[val] = parent[parent[val]]
        val = parent[val]
    return val


def union(val1: int, val2: int, parent: list, size: list) -> bool:
    ra, rb = find(val1, parent), find(val2, parent)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True


def part_one(input_data: str):
    points = []
    for l in input_data.strip().splitlines():
        x, y, z = map(int, l.split(','))
        points.append((x, y, z))

    n = len(points)
    parent = list(range(n))
    size = [1] * n

    pairs = []
    for i in range(n):
        x, y, z = points[i]
        for j in range(i + 1, n):
            xn, yn, zn = points[j]
            d = (x - xn) ** 2 + (y - yn) ** 2 + (z - zn) ** 2
            pairs.append((d, i, j))

    pairs.sort(key=lambda p: p[0])
    for _, a, b in pairs[:1000]:
        union(a, b, parent, size)

    components = {}
    for i in range(n):
        r = find(i, parent)
        components[r] = components.get(r, 0) + 1

    res = sorted(components.values(), reverse=True)[:3]
    while len(res) < 3:
        res.append(1)

    return math.prod(res)


def part_two(input_data: str):
    points = []
    for l in input_data.strip().splitlines():
        x, y, z = map(int, l.split(','))
        points.append((x, y, z))

    n = len(points)
    parent = list(range(n))
    size = [1] * n
    components = n

    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            pairs.append((d, i, j))

    pairs.sort(key=lambda p: p[0])
    for _, a, b in pairs:
        if union(a, b, parent, size):
            components -= 1
            if components == 1:
                return points[a][0] * points[b][0]


data = get_input_data(year=2025, task_number=8)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
