from itertools import product

import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

from get_input_data import get_input_data


def solve_machine(diagram, buttons):
    target_str = diagram.strip('[]')
    target = [1 if ch == '#' else 0 for ch in target_str]
    n_lights = len(target)
    n_buttons = len(buttons)

    matrix = [[0] * n_buttons for _ in range(n_lights)]
    for btn_idx, btn in enumerate(buttons):
        for light_idx in btn:
            matrix[light_idx][btn_idx] = 1

    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]
    pivots = []
    row = 0

    for col in range(n_buttons):
        pivot_row = None
        for r in range(row, n_lights):
            if aug[r][col] == 1:
                pivot_row = r
                break

        if pivot_row is None:
            continue

        aug[row], aug[pivot_row] = aug[pivot_row], aug[row]

        for r in range(row + 1, n_lights):
            if aug[r][col] == 1:
                for c in range(n_buttons + 1):
                    aug[r][c] = (aug[r][c] + aug[row][c]) % 2

        pivots.append((row, col))
        row += 1
        if row >= n_lights:
            break

    for r in range(row, n_lights):
        if aug[r][n_buttons] != 0:
            return 0

    pivot_cols = {col for _, col in pivots}
    free_vars = [col for col in range(n_buttons) if col not in pivot_cols]

    solution = [0] * n_buttons

    for r in range(len(pivots) - 1, -1, -1):
        pivot_row, pivot_col = pivots[r]
        val = aug[pivot_row][n_buttons]
        for c in range(pivot_col + 1, n_buttons):
            val = (val + aug[pivot_row][c] * solution[c]) % 2
        solution[pivot_col] = val

    if free_vars:
        min_presses = float('inf')
        for free_vals in product([0, 1], repeat=len(free_vars)):
            test_solution = solution[:]
            for i, col in enumerate(free_vars):
                test_solution[col] = free_vals[i]

            for r in range(len(pivots) - 1, -1, -1):
                pivot_row, pivot_col = pivots[r]
                val = aug[pivot_row][n_buttons]
                for c in range(pivot_col + 1, n_buttons):
                    val = (val + aug[pivot_row][c] * test_solution[c]) % 2
                test_solution[pivot_col] = val

            if all(sum(matrix[i][j] * test_solution[j] for j in range(n_buttons)) % 2 == target[i]
                   for i in range(n_lights)):
                min_presses = min(min_presses, sum(test_solution))

        return min_presses if min_presses != float('inf') else 0
    else:
        return sum(solution)


def solve_joltage_scipy(buttons, target):
    n_counters = len(target)
    n_buttons = len(buttons)

    a = np.zeros((n_counters, n_buttons), dtype=int)
    for btn_idx, btn in enumerate(buttons):
        for cnt_idx in btn:
            a[cnt_idx, btn_idx] = 1

    c = np.ones(n_buttons)
    bounds = Bounds(lb=0, ub=np.inf)
    constraints = LinearConstraint(a, lb=target, ub=target)
    result = milp(c=c, constraints=constraints,
                  bounds=bounds, integrality=[1] * n_buttons)

    if result.success:
        return int(round(result.fun))


def solve_joltage_machine(buttons, target):
    scipy_result = solve_joltage_scipy(buttons, target)
    if scipy_result is not None:
        return scipy_result

    n_counters = len(target)
    n_buttons = len(buttons)

    if all(t == 0 for t in target):
        return 0

    matrix = [[0] * n_buttons for _ in range(n_counters)]
    for btn_idx, btn in enumerate(buttons):
        for cnt_idx in btn:
            matrix[cnt_idx][btn_idx] = 1

    solution = [0] * n_buttons

    def solve_lim(max_presses, depth, part_state):
        if depth == n_buttons:
            return part_state == target

        current = sum(solution[:depth])
        if current >= max_presses:
            return False

        remaining = max_presses - current
        max_val = remaining

        for i in range(n_counters):
            if matrix[i][depth] > 0:
                needed = target[i] - part_state[i]
                if needed < 0:
                    return False
                max_val = min(max_val, needed)

        if max_val < 0:
            return False

        for val in range(min(max_val + 1, remaining + 1)):
            solution[depth] = val
            new_state = part_state[:]
            for i in range(n_counters):
                if matrix[i][depth] > 0:
                    new_state[i] += val
                    if new_state[i] > target[i]:
                        solution[depth] = 0
                        return False

            if solve_lim(max_presses, depth + 1, new_state):
                return True

        solution[depth] = 0
        return False

    partial_state = [0] * n_counters
    for limit in range(1, sum(target) + 50):
        if solve_lim(limit, 0, partial_state):
            return limit

    return 0


def part_one(input_data: str):
    total = 0

    for l in input_data.strip().splitlines():
        start = l.index('[')
        end = l.index(']')
        diagram = l[start:end + 1]

        buttons = []
        i = 0
        while i < len(l):
            if l[i] == '(':
                j = i + 1
                while j < len(l) and l[j] != ')':
                    j += 1
                btn_str = l[i + 1:j]
                indices = [int(x.strip()) for x in btn_str.split(',')]
                buttons.append(tuple(indices))
                i = j + 1
            else:
                i += 1

        total += solve_machine(diagram, buttons)

    return total


def part_two(input_data: str):
    total = 0

    for l in input_data.strip().splitlines():
        buttons = []
        i = 0
        while i < len(l):
            if l[i] == '(':
                j = i + 1
                while j < len(l) and l[j] != ')':
                    j += 1
                btn_str = l[i + 1:j]
                indices = [int(x.strip()) for x in btn_str.split(',')]
                buttons.append(tuple(indices))
                i = j + 1
            else:
                i += 1

        start = l.index('{')
        end = l.index('}')
        joltage_str = l[start + 1:end]
        target = [int(x.strip()) for x in joltage_str.split(',')]

        total += solve_joltage_machine(buttons, target)

    return total


data = get_input_data(year=2025, task_number=10)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
