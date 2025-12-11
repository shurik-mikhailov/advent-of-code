from functools import lru_cache

from get_input_data import get_input_data


def part_one(input_data: str) -> int:
    graph = {}
    for l in input_data.splitlines():
        name, outs = l.strip().split(":")
        outs = outs.strip().split()
        graph[name.strip()] = outs

    @lru_cache(None)
    def dfs(val):
        if val == "out":
            return 1
        if val not in graph:
            return 0
        total = 0
        for n_val in graph[val]:
            total += dfs(n_val)
        return total

    return dfs("you")


def part_two(input_data: str) -> int:
    graph = {}
    for l in input_data.splitlines():
        name, outs = l.strip().split(":")
        outs = outs.strip().split()
        graph[name.strip()] = outs

    @lru_cache(None)
    def count_paths(val1: str, val2: str):
        if val1 == val2:
            return 1
        total = 0
        for n_val in graph.get(val1, []):
            total += count_paths(n_val, val2)
        return total

    svr_fft = count_paths("svr", "fft")
    fft_dac = count_paths("fft", "dac")
    dac_out = count_paths("dac", "out")

    svr_dac = count_paths("svr", "dac")
    dac_fft = count_paths("dac", "fft")
    fft_out = count_paths("fft", "out")

    return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out


data = get_input_data(year=2025, task_number=11)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
