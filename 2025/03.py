from get_input_data import get_input_data


def part_one(input_data: str):
    total = 0

    for l in input_data.strip().splitlines():
        s = l.strip()
        if len(s) == 1:
            continue
        max_lead = int(s[0])
        best = -1
        for ch in s[1:]:
            d = int(ch)
            _ = max_lead * 10 + d
            if _ > best:
                best = _
            if d > max_lead:
                max_lead = d
        total += best

    return total


def part_two(input_data: str):
    total = 0

    for l in input_data.strip().splitlines():
        s = l.strip()
        k = 12
        n = len(s)
        drop = n - k,
        st = []
        for i, ch in enumerate(s):
            d = ch
            while st and drop > 0 and st[-1] < d:
                st.pop()
                drop -= 1
            st.append(d)

        total += int("".join(st[:k]))

    return total


data = get_input_data(year=2025, task_number=3)
print(f'part one: {part_one(input_data=data)}')
print(f'part two: {part_two(input_data=data)}')
