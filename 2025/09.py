from itertools import combinations

from shapely.geometry import Polygon, box

from get_input_data import get_input_data


def part_one(input_data: str) -> int:
    points = []
    for line in input_data.strip().splitlines():
        x, y = map(int, line.split(','))
        points.append((x, y))

    max_area = 0
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i + 1, len(points)):
            p2 = points[j]
            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if area > max_area:
                max_area = area

    return max_area


def part_two(input_data: str) -> int:
    points = []
    for line in input_data.strip().splitlines():
        x, y = map(int, line.split(','))
        points.append((x, y))

    max_area = 0
    poly = Polygon(points + [points[0]])
    for p1, p2 in combinations(points, 2):
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        rect = box(x_min, y_min, x_max, y_max)
        if rect.within(poly):
            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            if area > max_area:
                max_area = area

    return max_area


data = get_input_data(year=2025, task_number=9)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
