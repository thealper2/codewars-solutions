import re


def is_cubic(n):
    return n == sum(int(d) ** 3 for d in str(n))


def is_sum_of_cubes(s):
    chunks = []
    for run in re.findall(r'\d+', s):
        for i in range(0, len(run), 3):
            chunks.append(run[i:i + 3])

    cubics = [int(c) for c in chunks if is_cubic(int(c))]
    if not cubics:
        return "Unlucky"

    total = sum(cubics)
    return ' '.join(str(x) for x in cubics) + f' {total} Lucky'